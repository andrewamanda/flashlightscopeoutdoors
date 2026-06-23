# middleware.py
from django.core.cache import cache
from django.http import JsonResponse
import time

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.method == 'POST':
            ip = self.get_client_ip(request)
            key = f"ratelimit:{ip}"
            
            # Allow 5 POST requests per minute per IP
            current = cache.get(key, 0)
            if current >= 4:
                return JsonResponse({
                    'error': 'Rate limit exceeded. Please try again later.'
                }, status=429)
            
            cache.set(key, current + 1, 60)  # 60 seconds TTL
        
        return self.get_response(request)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


# comprehensive_security_middleware.py
from django.core.cache import cache
from django.http import JsonResponse
import hashlib
import time

class ComprehensiveSecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.method == 'POST':
            # Get client identification
            ip = self.get_client_ip(request)
            fingerprint = self.get_client_fingerprint(request)
            
            # Step 1: Check if IP is currently banned
            ban_result = self.check_ip_ban(ip)
            if ban_result:
                return ban_result
            
            # Step 2: Check rate limits
            rate_limit_result = self.check_rate_limits(fingerprint, ip, request)
            if rate_limit_result:
                # Increment violation count when rate limit is hit
                self.record_violation(ip, fingerprint)
                return rate_limit_result
            
            # Step 3: Check for suspicious patterns
            suspicious_result = self.check_suspicious_patterns(request)
            if suspicious_result:
                self.record_violation(ip, fingerprint)
                return suspicious_result
        
        response = self.get_response(request)
        
        # If downstream middleware or views return 429, count as violation
        if request.method == 'POST' and response.status_code == 429:
            ip = self.get_client_ip(request)
            fingerprint = self.get_client_fingerprint(request)
            self.record_violation(ip, fingerprint)
            
        return response
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR', '')
        return ip
    
    def get_client_fingerprint(self, request):
        """Create a fingerprint using multiple factors"""
        ip = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
        accept = request.META.get('HTTP_ACCEPT', '')
        
        fingerprint_string = f"{ip}-{user_agent}-{accept_language}-{accept}"
        return hashlib.md5(fingerprint_string.encode()).hexdigest()
    
    def check_ip_ban(self, ip):
        """Check if IP is temporarily banned"""
        if not ip:
            return None
            
        ban_key = f"ip_ban:{ip}"
        ban_until = cache.get(ban_key)
        
        if ban_until and time.time() < ban_until:
            remaining_time = int(ban_until - time.time())
            return JsonResponse({
                'error': f'IP temporarily banned. Try again in {remaining_time} seconds.'
            }, status=429)
        
        return None
    
    def check_rate_limits(self, fingerprint, ip, request):
        """Check multiple rate limiting strategies"""
        
        # Strategy 1: Short-term burst protection (per minute)
        burst_key = f"rate_burst:{fingerprint}"
        burst_count = cache.get(burst_key, 0)
        if burst_count >= 5:  # 5 requests per minute
            return JsonResponse({'error': 'Rate limit exceeded'}, status=429)
        cache.set(burst_key, burst_count + 1, 60)  # 1 minute TTL
        
        # Strategy 2: Medium-term protection (per hour)
        hourly_key = f"rate_hourly:{fingerprint}"
        hourly_count = cache.get(hourly_key, 0)
        if hourly_count >= 50:  # 50 requests per hour
            return JsonResponse({'error': 'Hourly rate limit exceeded'}, status=429)
        cache.set(hourly_key, hourly_count + 1, 3600)  # 1 hour TTL
        
        # Strategy 3: IP-based daily limit
        daily_ip_key = f"rate_daily_ip:{ip}"
        daily_ip_count = cache.get(daily_ip_key, 0)
        if daily_ip_count >= 200:  # 200 requests per day per IP
            return JsonResponse({'error': 'Daily limit exceeded'}, status=429)
        cache.set(daily_ip_key, daily_ip_count + 1, 86400)  # 24 hour TTL
        
        return None
    
    def check_suspicious_patterns(self, request):
        """Detect suspicious request patterns"""
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        
        # Missing or very short user agent
        if not user_agent or len(user_agent) < 10:
            return JsonResponse({'error': 'Invalid request'}, status=400)
        
        # Common bot user agents
        bot_indicators = ['bot', 'crawler', 'spider', 'python', 'curl', 'wget', 
                         'scrapy', 'requests', 'java', 'go-http-client']
        if any(indicator in user_agent for indicator in bot_indicators):
            return JsonResponse({'error': 'Access denied'}, status=403)
        
        # Missing referrer on POST requests (could be direct API abuse)
        if not request.META.get('HTTP_REFERER') and not self.is_api_request(request):
            return JsonResponse({'error': 'Invalid request'}, status=400)
            
        return None
    
    def is_api_request(self, request):
        """Check if this is a legitimate API request"""
        path = request.path.lower()
        api_indicators = ['/api/', '/ajax/', '/json/']
        return any(indicator in path for indicator in api_indicators)
    
    def record_violation(self, ip, fingerprint):
        """Record a violation and apply bans if necessary"""
        if not ip:
            return
            
        violations_key = f"violations:{ip}"
        violations = cache.get(violations_key, 0) + 1
        cache.set(violations_key, violations, 86400)  # Keep for 24 hours
        
        # Apply bans based on violation count
        if violations >= 3:
            ban_durations = [300, 1800, 7200, 21600]  # 5min, 30min, 2h, 6h
            ban_index = min(violations - 3, len(ban_durations) - 1)
            ban_duration = ban_durations[ban_index]
            
            ban_key = f"ip_ban:{ip}"
            cache.set(ban_key, time.time() + ban_duration, ban_duration)
            
            # Also ban the fingerprint
            fingerprint_ban_key = f"fp_ban:{fingerprint}"
            cache.set(fingerprint_ban_key, time.time() + ban_duration, ban_duration)


# emergency_block_middleware.py
from django.http import JsonResponse

class EmergencyBlockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Immediate block list - add the attacking IP
        self.blocked_ips = {
            '137.220.145.206',  # The attacker IP
        }
        
        # You can also block IP ranges if needed
        self.blocked_ranges = [
            '137.220.',  # Block entire /16 range if attacks continue
        ]
        
    def __call__(self, request):
        client_ip = self.get_client_ip(request)
        
        # Immediate IP block
        if self.should_block_ip(client_ip):
            return JsonResponse({
                'error': 'Access denied'
            }, status=403)
        
        return self.get_response(request)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ips = [ip.strip() for ip in x_forwarded_for.split(',')]
            return ips[0]  # First IP in X-Forwarded-For is the client
        return request.META.get('REMOTE_ADDR', '')
    
    def should_block_ip(self, ip):
        # Exact IP match
        if ip in self.blocked_ips:
            return True
        
        # IP range match
        for ip_range in self.blocked_ranges:
            if ip.startswith(ip_range):
                return True
        
        return False

# fake_success_middleware.py
from django.http import JsonResponse
import time
from django.core.cache import cache

class FakeSuccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.blocked_ips = {'137.220.145.206'}
        
    def __call__(self, request):
        client_ip = self.get_real_ip(request)
        
        if self.should_block(client_ip, request):
            return self.fake_success_response(request)
        
        return self.get_response(request)
    
    def get_real_ip(self, request):
        """Get the real client IP address"""
        xff = request.META.get('HTTP_X_FORWARDED_FOR')
        if xff:
            # Get the first IP in the list (original client)
            ips = [ip.strip() for ip in xff.split(',')]
            return ips[0]
        return request.META.get('REMOTE_ADDR', '')
    
    def should_block(self, ip, request):
        """Check if we should block this request"""
        # Block known attacker IP
        if ip in self.blocked_ips:
            return True
            
        # Aggressive rate limiting for POST requests
        if request.method == 'POST':
            key = f"post_limit:{ip}"
            count = cache.get(key, 0)
            if count >= 5:  # Only 5 POSTs per minute allowed
                return True
            cache.set(key, count + 1, 60)  # 60 second TTL
            
        return False
    
    def fake_success_response(self, request):
        """Return fake success response that looks legitimate"""
        fake_data = {
            "status": "success",
            "message": "Request processed successfully",
            "id": "000000",
            "timestamp": int(time.time())
        }
        
        # Customize response based on the endpoint if needed
        if 'checkout' in request.path:
            fake_data["redirect_url"] = "/checkout/success/"
            fake_data["order_id"] = "ORD-000000"
        elif 'api' in request.path:
            fake_data["data"] = {"processed": True, "id": "0000"}
            
        return JsonResponse(fake_data, status=200)  # 200 status won't trigger emails


# fingerprint_blocker.py
import hashlib
import re
import json
from django.http import JsonResponse
from django.core.cache import cache
import time



class ExceptionEmailMiddleware:
    """Send admin error email for unhandled exceptions when DEBUG=False, then re-raise.

    This restores the production behavior you want: customers see the generic
    500 page, while ADMINS receive the traceback by email. It does not replace
    Django's normal exception handling; it only makes the email notification
    independent of the logging configuration.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except Exception:
            from django.conf import settings
            if not getattr(settings, 'DEBUG', False):
                try:
                    import traceback
                    from django.core.mail import mail_admins

                    subject = 'Server error: %s %s' % (request.method, request.get_full_path())
                    message = (
                        'Unhandled exception on production server.\n\n'
                        'Method: %s\n'
                        'Path: %s\n'
                        'User: %s\n'
                        'IP: %s\n\n'
                        'Traceback:\n%s'
                    ) % (
                        request.method,
                        request.get_full_path(),
                        getattr(request, 'user', None),
                        request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR', ''),
                        traceback.format_exc(),
                    )
                    mail_admins(subject, message, fail_silently=True)
                except Exception:
                    # Never let the notification path change the customer's response.
                    pass
            raise

class FingerprintBlockerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Pre-load known attacker patterns
        self.known_bad_patterns = [
            '@@YuAIi', '137.220.145.206', 
            'python', 'curl', 'wget', 'requests'
        ]
        
    def __call__(self, request):
        # Skip fingerprinting for GET requests to reduce overhead
        if request.method != 'POST':
            return self.get_response(request)
            
        fingerprint = self.create_comprehensive_fingerprint(request)
        
        if self.should_block(fingerprint, request):
            # Log the block for analysis
            self.log_attack_attempt(fingerprint, request)
            return self.fake_success_response()
        
        return self.get_response(request)
    
    def create_comprehensive_fingerprint(self, request):
        """Create a unique fingerprint based on multiple request attributes"""
        components = []
        
        # 1. NETWORK CHARACTERISTICS
        components.extend(self.get_network_fingerprint(request))
        
        # 2. HEADER PATTERNS
        components.append(self.get_header_pattern_fingerprint(request))
        
        # 3. BEHAVIORAL PATTERNS
        components.append(self.get_behavioral_fingerprint(request))
        
        # 4. CONTENT PATTERNS (if any POST data)
        components.append(self.get_content_fingerprint(request))
        
        fingerprint_string = '|'.join(str(c) for c in components)
        return hashlib.sha256(fingerprint_string.encode()).hexdigest()
    
    def get_network_fingerprint(self, request):
        """Fingerprint based on network characteristics"""
        network_data = []
        
        # Extract ALL IPs from all headers
        all_ips = []
        for header in ['HTTP_X_FORWARDED_FOR', 'REMOTE_ADDR', 'HTTP_X_REAL_IP']:
            value = request.META.get(header, '')
            if value:
                ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', value)
                all_ips.extend(ips)
        
        network_data.append(','.join(sorted(set(all_ips))))
        
        # IP pattern analysis
        xff = request.META.get('HTTP_X_FORWARDED_FOR', '')
        if '@@' in xff:
            network_data.append('MALICIOUS_XFF_PATTERN')
        
        return network_data
    
    def get_header_pattern_fingerprint(self, request):
        """Analyze header patterns and anomalies"""
        header_patterns = []
        
        # User Agent analysis
        ua = request.META.get('HTTP_USER_AGENT', '')
        if not ua or len(ua) < 10:
            header_patterns.append('MISSING_UA')
        elif any(pattern in ua.lower() for pattern in ['python', 'curl', 'wget']):
            header_patterns.append('SCRIPT_UA')
        
        # Accept header patterns
        accept = request.META.get('HTTP_ACCEPT', '')
        if 'application/json' in accept and 'text/html' not in accept:
            header_patterns.append('API_CLIENT')
        
        # Referrer analysis for POST requests
        referrer = request.META.get('HTTP_REFERER', '')
        if not referrer and request.method == 'POST':
            header_patterns.append('MISSING_REFERRER')
        
        # X-Forwarded-For anomalies
        xff = request.META.get('HTTP_X_FORWARDED_FOR', '')
        if len(xff) > 100:
            header_patterns.append('LONG_XFF')
        if xff.count(',') > 5:
            header_patterns.append('MANY_PROXIES')
        
        return ','.join(header_patterns)
    
    def get_behavioral_fingerprint(self, request):
        """Fingerprint based on request behavior"""
        behavioral_patterns = []
        
        # Request timing (you could add more sophisticated timing analysis)
        behavioral_patterns.append(str(int(time.time()) // 300))  # 5-minute window
        
        # Request path patterns
        path = request.path
        if '/api/' in path:
            behavioral_patterns.append('API_PATH')
        if 'checkout' in path:
            behavioral_patterns.append('CHECKOUT_PATH')
        
        # Method pattern
        behavioral_patterns.append(request.method)
        
        return ','.join(behavioral_patterns)
    
    def get_content_fingerprint(self, request):
        """Analyze POST content patterns"""
        if not request.POST:
            return 'NO_POST_DATA'
        
        content_indicators = []
        
        # Check for common form fields (bots often miss some)
        expected_fields = ['csrfmiddlewaretoken', 'submit', 'email']
        missing_fields = [field for field in expected_fields if field not in request.POST]
        if missing_fields:
            content_indicators.append(f'MISSING_{len(missing_fields)}_FIELDS')
        
        # Check data patterns
        post_data_str = json.dumps(dict(request.POST))
        if len(post_data_str) > 1000:
            content_indicators.append('LARGE_POST')
        
        return ','.join(content_indicators)
    
    def should_block(self, fingerprint, request):
        """Determine if request should be blocked"""
        # 1. Check if fingerprint is already banned
        if cache.get(f"banned_fp:{fingerprint}"):
            return True
        
        # 2. Check for immediate red flags
        if self.has_immediate_red_flags(request):
            self.ban_fingerprint(fingerprint, 86400)  # Ban for 24 hours
            return True
        
        # 3. Rate limiting by fingerprint
        request_count = self.get_fingerprint_request_count(fingerprint)
        if request_count > 5:  # More than 5 requests in 10 minutes
            self.ban_fingerprint(fingerprint, 3600)  # Ban for 1 hour
            return True
        
        # 4. Pattern-based detection
        if self.detect_malicious_patterns(request):
            self.ban_fingerprint(fingerprint, 7200)  # Ban for 2 hours
            return True
        
        return False
    
    def has_immediate_red_flags(self, request):
        """Check for obvious attack signatures"""
        xff = request.META.get('HTTP_X_FORWARDED_FOR', '').lower()
        
        # Your specific attacker pattern
        if '@@yuaii' in xff and '137.220.145.206' in xff:
            return True
        
        # SQL injection patterns in headers
        sql_keywords = ['union', 'select', 'drop', 'insert', 'update', 'delete']
        if any(keyword in xff for keyword in sql_keywords):
            return True
        
        # Suspicious user agents
        ua = request.META.get('HTTP_USER_AGENT', '').lower()
        if not ua or any(pattern in ua for pattern in ['python', 'curl', 'wget']):
            return True
        
        return False
    
    def detect_malicious_patterns(self, request):
        """Detect more subtle malicious patterns"""
        # Multiple IPs in X-Forwarded-For with garbage data
        xff = request.META.get('HTTP_X_FORWARDED_FOR', '')
        if xff.count(',') > 3 and len(xff) > 50:
            return True
        
        # Missing common headers that browsers send
        expected_headers = ['HTTP_USER_AGENT', 'HTTP_ACCEPT', 'HTTP_ACCEPT_LANGUAGE']
        missing_count = sum(1 for header in expected_headers if not request.META.get(header))
        if missing_count > 1:
            return True
        
        return False
    
    def get_fingerprint_request_count(self, fingerprint):
        """Get number of requests for this fingerprint in last 10 minutes"""
        key = f"fp_count:{fingerprint}"
        count = cache.get(key, 0)
        cache.set(key, count + 1, 600)  # 10 minute window
        return count + 1
    
    def ban_fingerprint(self, fingerprint, duration):
        """Ban a fingerprint for specified duration"""
        cache.set(f"banned_fp:{fingerprint}", True, duration)
    
    def log_attack_attempt(self, fingerprint, request):
        """Log attack attempts for analysis"""
        # You can implement logging to file, database, or monitoring system
        print(f"Blocked attack - Fingerprint: {fingerprint}, Path: {request.path}, IP: {request.META.get('REMOTE_ADDR')}")
    
    def fake_success_response(self):
        """Return fake success response"""
        return JsonResponse({
            'status': 'success',
            'message': 'Request processed successfully',
            'timestamp': int(time.time())
        }, status=200)

# pattern_blocker_middleware.py
import re
from django.http import JsonResponse

class PatternBlockerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.malicious_patterns = [
            r'@@.*\d+\.\d+\.\d+\.\d+',  # Pattern like @@YuAIi, 137.220.145.206
            r'[^0-9.,\s]+\s*,\s*\d+\.\d+\.\d+\.\d+',  # Non-IP text before IP
            r'script|alert|union|select|drop|insert',  # SQL injection patterns
        ]
        
    def __call__(self, request):
        if self.is_malicious_request(request):
            return JsonResponse({'status': 'success'}, status=200)
        
        return self.get_response(request)
    
    def is_malicious_request(self, request):
        """Check for malicious request patterns"""
        xff = request.META.get('HTTP_X_FORWARDED_FOR', '')
        
        # Check for known malicious patterns in X-Forwarded-For
        for pattern in self.malicious_patterns:
            if re.search(pattern, xff, re.IGNORECASE):
                return True
        
        # Check for suspicious user agents
        ua = request.META.get('HTTP_USER_AGENT', '').lower()
        if not ua or 'python' in ua or 'curl' in ua or 'wget' in ua:
            return True
        
        # Check for missing or suspicious referrer on POST requests
        if request.method == 'POST':
            referrer = request.META.get('HTTP_REFERER', '')
            if not referrer or 'http' not in referrer:
                return True
        
        return False


# robust_ip_middleware.py
import re
from django.http import JsonResponse
from django.core.cache import cache
import time

class RobustIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.known_attacker_ips = {'137.220.145.206'}
        self.suspicious_patterns = re.compile(r'@@|YuAIi|script|alert|union|select', re.IGNORECASE)
        
    def __call__(self, request):
        client_ips = self.get_valid_ips(request)
        
        # Check all extracted IPs
        for ip in client_ips:
            if self.should_block(ip, request):
                return self.fake_success_response()
        
        # Also check the raw header for suspicious content
        if self.has_suspicious_header(request):
            return self.fake_success_response()
        
        return self.get_response(request)
    
    def get_valid_ips(self, request):
        """Extract and validate all IP addresses from headers"""
        valid_ips = []
        
        # Check X-Forwarded-For header
        xff = request.META.get('HTTP_X_FORWARDED_FOR', '')
        if xff:
            # Split and clean each part
            parts = [part.strip() for part in xff.split(',')]
            for part in parts:
                ip = self.extract_valid_ip(part)
                if ip:
                    valid_ips.append(ip)
        
        # Check other possible IP headers
        for header in ['REMOTE_ADDR', 'HTTP_X_REAL_IP', 'HTTP_CF_CONNECTING_IP']:
            ip = request.META.get(header, '')
            if ip:
                valid_ip = self.extract_valid_ip(ip)
                if valid_ip:
                    valid_ips.append(valid_ip)
        
        return valid_ips
    
    def extract_valid_ip(self, ip_string):
        """Extract valid IP address from potentially malformed string"""
        # Remove any non-IP characters and extract IP pattern
        ip_match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', ip_string)
        if ip_match:
            ip = ip_match.group()
            # Validate it's a real IP (not 0.0.0.0, etc.)
            if self.is_valid_ipv4(ip):
                return ip
        return None
    
    def is_valid_ipv4(self, ip):
        """Validate IPv4 address"""
        try:
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255:
                    return False
            # Check for private/local IPs if needed
            if ip.startswith('0.') or ip.startswith('127.') or ip.startswith('10.') or \
               ip.startswith('192.168.') or (ip.startswith('172.') and 16 <= int(ip.split('.')[1]) <= 31):
                return False
            return True
        except:
            return False
    
    def has_suspicious_header(self, request):
        """Check for suspicious header content"""
        xff = request.META.get('HTTP_X_FORWARDED_FOR', '').lower()
        
        # Check for known attack patterns
        suspicious_indicators = ['@@', 'yuaii', 'script', 'alert', 'union', 'select', '<', '>', '../']
        if any(indicator in xff for indicator in suspicious_indicators):
            return True
        
        # Check for obviously malformed headers
        if len(xff) > 1000:  # Excessively long header
            return True
            
        if xff.count(',') > 10:  # Too many IPs in chain
            return True
            
        return False
    
    def should_block(self, ip, request):
        """Check if IP should be blocked"""
        # Block known attacker IPs
        if ip in self.known_attacker_ips:
            return True
        
        # Block entire IP ranges if needed
        if ip.startswith('137.220.'):  # Block entire /16 range
            return True
        
        # Rate limiting for POST requests
        if request.method == 'POST':
            key = f"post_limit:{ip}"
            count = cache.get(key, 0)
            if count >= 3:  # 3 POSTs per minute
                return True
            cache.set(key, count + 1, 60)
        
        return False
    
    def fake_success_response(self):
        """Return fake success response"""
        return JsonResponse({
            'status': 'success',
            'message': 'Request processed successfully',
            'timestamp': int(time.time())
        }, status=200)

# attack_monitor.py
class AttackMonitorMiddleware:
    """Logs and analyzes attack patterns - add this last in the chain"""
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)

        # Static/media responses are often streaming FileResponses in development.
        # Accessing response.content on those can raise and turn a valid asset request
        # into a 500 error, so only inspect non-streaming responses safely.
        try:
            should_log = hasattr(request, 'was_blocked')
            if not should_log and response.status_code == 200 and not getattr(response, 'streaming', False):
                content = getattr(response, 'content', b'')
                if isinstance(content, bytes):
                    body = content.decode(errors='ignore').lower()
                else:
                    body = str(content).lower()
                should_log = 'success' in body
            if should_log:
                self.log_blocked_request(request)
        except Exception:
            # Monitoring must never break normal responses.
            pass
        
        return response
    
    def log_blocked_request(self, request):
        """Log details about blocked requests"""
        # Implement your logging logic here
        pass
