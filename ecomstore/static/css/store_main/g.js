/* Minified webstore.js, selectall.js, calendar1.js, carousel.js, tabs.js, ga_social_tracking.js, lightbox.js */
var Placeholders = (function() {
    var o = ["text", "search", "url", "tel", "email", "password", "number", "textarea"],
        f = {
            live: false,
            hideOnFocus: false
        }, i = [37, 38, 39, 40],
        d, c;

    function m(r) {
        var q;
        if (r.createTextRange) {
            q = r.createTextRange();
            q.move("character", 0);
            q.select()
        } else {
            if (r.selectionStart) {
                r.focus();
                r.setSelectionRange(0, 0)
            }
        }
    }

    function k() {
        var q;
        if (this.value === this.getAttribute("placeholder")) {
            if (!f.hideOnFocus) {
                m(this)
            } else {
                this.className = this.className.replace(/\bplaceholderspolyfill\b/, "");
                this.value = "";
                q = this.getAttribute("data-placeholdertype");
                if (q) {
                    this.type = q
                }
                maxlength = this.getAttribute("data-maxlength");
                if (maxlength) {
                    this.maxLength = maxlength
                }
            }
        }
    }

    function j() {
        var q;
        if (this.value === "") {
            this.className = this.className + " placeholderspolyfill";
            this.value = this.getAttribute("placeholder");
            q = this.getAttribute("data-placeholdertype");
            if (q) {
                this.type = "text"
            }
            maxlength = this.getAttribute("data-maxlength");
            if (maxlength) {
                this.maxLength = this.value.length + 1
            }
        }
    }

    function n() {
        var s = this.getElementsByTagName("input"),
            q = this.getElementsByTagName("textarea"),
            r = s.length,
            t = r + q.length,
            v, w, u;
        for (u = 0; u < t; u += 1) {
            v = (u < r) ? s[u] : q[u - r];
            w = v.getAttribute("placeholder");
            if (v.value === w) {
                v.value = ""
            }
        }
    }

    function l(q) {
        c = this.value;
        return !(c === this.getAttribute("placeholder") && i.indexOf(q.keyCode) > -1)
    }

    function a() {
        var q;
        if (this.value !== c) {
            this.className = this.className.replace(/\bplaceholderspolyfill\b/, "");
            this.value = this.value.replace(this.getAttribute("placeholder"), "");
            q = this.getAttribute("data-placeholdertype");
            if (q) {
                this.type = q
            }
            maxlength = this.getAttribute("data-maxlength");
            if (maxlength) {
                this.maxLength = maxlength
            }
        }
        if (this.value === "") {
            j.call(this);
            m(this)
        }
    }

    function g(q, s, r) {
        if (q.addEventListener) {
            return q.addEventListener(s, r.bind(q), false)
        }
        if (q.attachEvent) {
            return q.attachEvent("on" + s, r.bind(q))
        }
    }

    function e(q) {
        if (!f.hideOnFocus) {
            g(q, "keydown", l);
            g(q, "keyup", a)
        }
        g(q, "focus", k);
        g(q, "blur", j)
    }

    function h() {
        var w = document.getElementsByTagName("input"),
            y = document.getElementsByTagName("textarea"),
            r = w.length,
            u = r + y.length,
            s, q, t, x, v;
        for (s = 0; s < u; s += 1) {
            t = (s < r) ? w[s] : y[s - r];
            v = t.getAttribute("placeholder");
            if (o.indexOf(t.type) > -1) {
                if (v) {
                    x = t.getAttribute("data-currentplaceholder");
                    if (v !== x) {
                        if (t.value === x || t.value === v || !t.value) {
                            t.value = v;
                            t.className = t.className + " placeholderspolyfill"
                        }
                        if (!x) {
                            if (t.form) {
                                q = t.form;
                                if (!q.getAttribute("data-placeholdersubmit")) {
                                    g(q, "submit", n);
                                    q.setAttribute("data-placeholdersubmit", "true")
                                }
                            }
                            e(t)
                        }
                        t.setAttribute("data-currentplaceholder", v)
                    }
                }
            }
        }
    }

    function b() {
        var v = document.getElementsByTagName("input"),
            x = document.getElementsByTagName("textarea"),
            r = v.length,
            u = r + x.length,
            s, t, q, y;
        for (s = 0; s < u; s += 1) {
            t = (s < r) ? v[s] : x[s - r];
            y = t.getAttribute("placeholder");
            if (o.indexOf(t.type) > -1) {
                if (y) {
                    if (t.type === "password") {
                        try {
                            t.type = "text";
                            t.setAttribute("data-placeholdertype", "password")
                        } catch (w) {}
                    }
                    t.setAttribute("data-currentplaceholder", y);
                    if (t.value === "" || t.value === y) {
                        if (t.maxLength && t.maxLength <= y.length) {
                            t.setAttribute("data-maxlength", t.maxLength);
                            t.maxLength = y.length + 1
                        }
                        t.className = t.className + " placeholderspolyfill";
                        t.value = y
                    }
                    if (t.form) {
                        q = t.form;
                        if (!q.getAttribute("data-placeholdersubmit")) {
                            g(q, "submit", n);
                            q.setAttribute("data-placeholdersubmit", "true")
                        }
                    }
                    e(t)
                }
            }
        }
    }

    function p(u) {
        var w = document.createElement("input"),
            t, v, s, r, q;
        if (typeof w.placeholder === "undefined") {
            for (t in u) {
                if (u.hasOwnProperty(t)) {
                    f[t] = u[t]
                }
            }
            v = document.createElement("style");
            v.type = "text/css";
            s = document.createTextNode(".placeholderspolyfill { color:#999 !important; }");
            if (v.styleSheet) {
                v.styleSheet.cssText = s.nodeValue
            } else {
                v.appendChild(s)
            }
            document.getElementsByTagName("head")[0].appendChild(v);
            if (!Array.prototype.indexOf) {
                Array.prototype.indexOf = function(x, y) {
                    for (r = (y || 0), q = this.length; r < q; r += 1) {
                        if (this[r] === x) {
                            return r
                        }
                    }
                    return -1
                }
            }
            if (!Function.prototype.bind) {
                Function.prototype.bind = function(x) {
                    if (typeof this !== "function") {
                        throw new TypeError("Function.prototype.bind - what is trying to be bound is not callable")
                    }
                    var B = Array.prototype.slice.call(arguments, 1),
                        A = this,
                        y = function() {}, z = function() {
                            return A.apply(this instanceof y ? this : x, B.concat(Array.prototype.slice.call(arguments)))
                        };
                    y.prototype = this.prototype;
                    z.prototype = new y();
                    return z
                }
            }
            b();
            if (f.live) {
                d = setInterval(h, 100)
            }
            return true
        }
        return false
    }
    return {
        init: p,
        refresh: h
    }
}());

function doOnLoad() {}

function log(a) {
    if (window.console) {
        console.log(a)
    }
}

function googleTranslateElementInit() {
    new google.translate.TranslateElement({
        pageLanguage: "en",
        autoDisplay: false,
        layout: google.translate.TranslateElement.InlineLayout.SIMPLE
    }, "google_translate_element")
}

function get_param(e) {
    var c = window.location.search.substring(1);
    if (c.indexOf("&") > -1) {
        var d = c.split("&");
        for (var b = 0; b < d.length; b++) {
            var a = d[b].split("=");
            if (a[0] == e) {
                return a[1]
            }
        }
    } else {
        var d = c.split("=");
        if (d[0] == e) {
            return d[1]
        }
    }
    return null
}

function clickclear(b, a) {
    if (b.value == a) {
        b.value = ""
    }
}

function clickrecall(b, a) {
    if (b.value == "") {
        b.value = a
    }
}

function switchCategoryImage(n, v, l, r, x, w, c, m, f) {
    var e = document.getElementById("productCategoryImage");
    var h = document.createElement("center");
    var s = document.getElementById("productCategoryVideo");
    var j = document.getElementById("optionImagesList");
    if (s) {
        s.style.display = "none"
    }
    if (j) {
        j.style.display = "none"
    }
    if ((v.indexOf("graciousstyle.com/images") > -1) || (v.indexOf("cloudfront.net/images") > -1)) {
        var k = document.createElement("img");
        k.src = v;
        k.vspace = 5;
        k.hspace = 5;
        k.border = 0;
        k.style.width = "420px";
        k.style.height = "auto";
        if (m) {
            k.alt = m
        }
        h.appendChild(k);
        h.appendChild(document.createElement("br"));
        if (r) {
            var b = document.createElement("div");
            b.style.height = "20px";
            var p = document.createElement("a");
            p.className = "viewLargerButton lightboxignore";
            p.rel = "lightbox[" + l + "categoryImages]";
            p.href = r;
            var o = document.createElement("img");
            o.src = x;
            o.style.border = 0;
            p.appendChild(o);
            var u = document.createElement("span");
            u.innerHTML = "<b>View Larger</b>";
            p.appendChild(u);
            b.appendChild(p);
            h.appendChild(b);
            if (f != null && f.length > 0) {
                var t = document.createElement("div");
                t.innerHTML = "<i>" + f + "</i>";
                t.setStyle("margin-bottom: 8px;");
                h.appendChild(t)
            }
        }
    } else {
        if (v === "colors") {
            if (j) {
                j.style.display = "block"
            }
        } else {
            if (s) {
                var d = v.indexOf(":");
                if (d > -1 && (d + 1) < v.length) {
                    var g = v.substring(d + 1, v.length);
                    if (g) {
                        g = g.replace(/^\s+|\s+$/g, "");
                        if (v.toLowerCase().indexOf("youtube:") > -1) {
                            g = "http://www.youtube.com/embed/" + g
                        } else {
                            if (v.toLowerCase().indexOf("vimeo:") > -1) {
                                g = "http://player.vimeo.com/video/" + g + "?title=0&byline=0&portrait=0"
                            }
                        }
                        s.src = g;
                        s.style.display = "block"
                    }
                }
            }
        }
    }
    for (var q = e.childNodes.length - 1; q >= 0; q--) {
        e.removeChild(e.childNodes[q])
    }
    e.appendChild(h);
    var a = document.getElementById("altCategoryImages").getElementsByTagName("a");
    for (var q = a.length - 1; q >= 0; q--) {
        if (a[q].className == "selectedAddImagesItem") {
            a[q].className = "selectableAddImagesItem"
        }
    }
    document.getElementById(n).className = "selectedAddImagesItem"
}

function hideAllWindows() {
    $$("div.popupWindow").each(function(a) {
        hideImageWindow(a)
    })
}

function showWindow(a) {
    var b = document.getElementById(a);
    b.style.visibility = "visible"
}

function showImageWindow(d, a, g, c, f) {
    var h = document.getElementById(g);
    var b = document.createElement("img");
    b.src = d;
    b.alt = "Image";
    b.style.borderColor = "#cccccc";
    b.style.borderStyle = "solid";
    b.style.borderSize = "2px";
    for (var e = h.childNodes.length - 1; e >= 0; e--) {
        h.removeChild(h.childNodes[e])
    }
    h.appendChild(b);
    win = document.getElementById(a);
    if (f) {
        win.onCloseZoomHandler = f
    }
    win.style.visibility = "visible";
    if (c) {
        c.call(this)
    }
}

function hideImageWindow(b) {
    var a = b;
    if (typeof b === "string") {
        a = document.getElementById(b)
    }
    a.style.visibility = "hidden";
    if (a.onCloseZoomHandler) {
        a.onCloseZoomHandler.call(this)
    }
}

function showProductImageWindow(b, a, d, c) {
    el = document.getElementById(c);
    win = document.getElementById(a);
    win.style.marginTop = getOffsetTop(el) - 350 + "px";
    showImageWindow(b, a, d)
}

function getOffsetTop(a) {
    var b = 0;
    while (a) {
        b = b + parseInt(a.offsetTop);
        a = a.offsetParent
    }
    return b
}

function validateEmail(a, c) {
    var b = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    if (b.test(a)) {
        return true
    }
    if (c) {
        alert(c)
    }
    return false
}

function activateSubmitIfValidEmail(d, c, e) {
    var b = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    var a = d.value;
    if (b.test(a)) {
        d.removeClassName("error");
        c.removeClassName("disabled");
        c.setAttribute("disabled", "");
        c.removeAttribute("disabled");
        if (d.form) {
            d.form._invalid = false
        }
    } else {
        if (!e || e != a) {
            d.addClassName("error")
        } else {
            d.removeClassName("error")
        }
        c.addClassName("disabled");
        c.addClassName("disabled");
        c.setAttribute("disabled", "disabled");
        if (d.form) {
            d.form._invalid = true
        }
    }
}

function activateSubmitIfValidEmailRecallDefault(b, a, c) {
    clickrecall(b, c);
    activateSubmitIfValidEmail(b, a, c)
}

function getScrollTop() {
    return (window.pageYOffset) ? window.pageYOffset : (document.documentElement && document.documentElement.scrollTop) ? document.documentElement.scrollTop : document.body.scrollTop
}

function padRect(f, g, h) {
    var d = f.top;
    var a = f.bottom;
    var c = f.left;
    var e = f.right;
    if (g) {
        c -= g;
        e += g
    }
    if (h) {
        d -= h;
        a += h
    }
    return {
        top: d,
        bottom: a,
        right: e,
        left: c
    }
}

function elementInViewport(c, e, f) {
    var d = padRect(c.getBoundingClientRect(), e, f);
    var b = window.innerWidth || (window.document.documentElement.clientWidth || window.document.body.clientWidth);
    var a = window.innerHeight || (window.document.documentElement.clientHeight || window.document.body.clientHeight);
    return (d.top >= 0 && d.left >= 0 && d.bottom <= a && d.right <= b)
}

function scrollElementInViewport(e, c, g) {
    if (elementInViewport(e, c, g)) {
        return
    }
    var i = padRect(e.getBoundingClientRect(), c, g);
    var d = window.innerWidth || (window.document.documentElement.clientWidth || window.document.body.clientWidth);
    var j = window.innerHeight || (window.document.documentElement.clientHeight || window.document.body.clientHeight);
    var n = 0;
    var m = 0;
    var k = i.top;
    var h = i.bottom;
    var f = i.left;
    var a = i.right;
    if (i.left < 0) {
        n = -f
    } else {
        if (i.right > d) {
            n = a - d
        }
    } if (i.top < 0) {
        m = -k
    } else {
        if (i.bottom > j) {
            m = h - j
        }
    }
    log("scrollBy " + n + " " + m);
    window.scrollBy(n, m)
}

function ie6iframehack(a) {
    if (!a) {
        return
    }
    var c = document.all && (navigator.userAgent.toLowerCase().indexOf("msie 6.") != -1);
    if (c) {
        var b = "<iframe class=\"bgiframe\" src=\"javascript:false;document.write('');\" tabindex=\"-1\" style=\"display:block; position:absolute; top: expression(((parseInt(this.parentNode.currentStyle.borderTopWidth)  || 0) * -1) + 'px'); left:expression(((parseInt(this.parentNode.currentStyle.borderLeftWidth) || 0) * -1) + 'px'); z-index:-1; filter:Alpha(Opacity='0'); width:expression(this.parentNode.offsetWidth + 'px'); height:expression(this.parentNode.offsetHeight + 'px')\"/>";
        a.innerHTML += b
    }
}

function loadBlogPost(b, d, a) {
    var c = $(a);
    if (c) {
        log("loadBlogPost: " + b + " " + d + " " + a);
        if (c.readAttribute("data-loading-blogpost") === "true") {
            log("loadBlogPost: " + b + " " + d + " " + a + " : already loading ...");
            return
        }
        if (c.readAttribute("data-loaded-blogpost") === "true") {
            log("loadBlogPost: " + b + " " + d + " " + a + " : already loaded ...");
            return
        }
        c.writeAttribute("data-loading-blogpost", "true");
        new Ajax.Request("/webstore/control/blogPostJSON", {
            method: "get",
            parameters: {
                blogSiteId: b,
                blogPostId: d
            },
            evalJSON: "force",
            onComplete: function(f) {
                var e = $(a);
                e.writeAttribute("data-loading-blogpost", "false")
            },
            onSuccess: function(f) {
                var e = $(a);
                e.innerHTML = f.responseJSON.postText + '<div class="endBlogPost"></div>';
                e.writeAttribute("data-loaded-blogpost", "true")
            }
        })
    }
}

function loadDisplayBlogPost(d, c, a) {
    var b = $(a);
    if (b) {
        log("loadDisplayBlogPost: " + d + " " + c + " " + a);
        if (b.readAttribute("data-loading-blogpost") === "true") {
            log("loadDisplayBlogPost: " + d + " " + c + " " + a + " : already loading ...");
            return
        }
        if (b.readAttribute("data-loaded-blogpost") === "true") {
            log("loadDisplayBlogPost: " + d + " " + c + " " + a + " : already loaded ...");
            return
        }
        b.writeAttribute("data-loading-blogpost", "true");
        new Ajax.Request("/webstore/control/displayBlogPostJSON", {
            method: "get",
            parameters: {
                blogKey: d,
                post: c
            },
            evalJSON: "force",
            onComplete: function(f) {
                var e = $(a);
                e.writeAttribute("data-loading-blogpost", "false")
            },
            onSuccess: function(f) {
                var e = $(a);
                e.innerHTML = f.responseJSON.postText + '<div class="endBlogPost"></div>';
                e.writeAttribute("data-loaded-blogpost", "true")
            }
        })
    }
}

function onRegistryChanged() {
    var a = document.getElementById("createNewRegistryCb");
    if (a && a.checked) {
        switchCreateRegistry(true)
    } else {
        switchCreateRegistry(false)
    }
}

function switchCreateRegistry(d) {
    var c = new Array("listName", "listName2", "shoppingListEventTypeId", "day", "month", "year");
    var b = document.getElementById("createRegistryForm");
    if (b) {
        b.className = d ? "" : "disabled";
        for (var a = 0; a < c.length; a++) {
            document.addItemsToRegistry[c[a]].disabled = !d
        }
    }
}

function redeemLoyaltyOnAddressChanged() {
    var a = document.getElementById("createNewAddressCb");
    if (a && a.checked) {
        redeemLoyaltySwitchCreateAddress(true)
    } else {
        redeemLoyaltySwitchCreateAddress(false)
    }
}

function redeemLoyaltySwitchCreateAddress(b) {
    var a = document.getElementById("loyaltyCreateShippingAddress");
    if (b) {
        a.style.display = "block"
    } else {
        a.style.display = "none"
    }
}

function submitAjaxCartFormAddToRegistry(c, f, b, a) {
    var d = $(f);
    var g = $(c);
    if (g.readAttribute("data-disabled") === "true") {
        return
    }
    d.addToRegistry.value = "Y";
    if (d.addToRegistryIndex) {
        d.addToRegistryIndex.value = b
    }
    submitAjaxCartForm(f, "addToRegistryPopup");
    d.addToRegistry.value = "N";
    if (d.addToRegistryIndex) {
        d.addToRegistryIndex.value = ""
    }
    if (a) {
        a()
    }
}

function getPopupCart() {
    var a = $("popupCart");
    if (!a) {
        a = new Element("div", {
            id: "popupCart"
        }).hide();
        document.body.appendChild(a)
    }
    return a
}

function submitAjaxCartForm(d, b, a) {
    var c = $(d);
    if (c.useAjax) {
        c.useAjax.value = "Y"
    }
    c.request({
        onComplete: function(f) {
            c.reset();
            disableFormQtyWhereNeeded(c);
            var e;
            if (a) {
                e = $(a)
            } else {
                e = getPopupCart()
            } if (b) {
                e.className = b
            } else {
                e.className = ""
            }
            e.update(f.responseText);
            ie6iframehack(document.getElementById("popupCart"));
            e.show();
            movePopupToView(e, 10)
        }
    })
}

function movePopupToView(d, c, a) {
    var b = getScrollTop();
    if (a) {
        b = a.cumulativeOffset().top
    }
    d.setStyle({
        top: (b + c) + "px"
    })
}

function showDropDown(d, b) {
    var c = $(d);
    if (c) {
        c.setStyle("font-weight: bold;")
    }
    c = $(d + "_bottom");
    if (c) {
        c.setStyle("font-weight: bold;");
        var a = document.getElementById(b + "_selected");
        a.innerHTML = c.innerHTML;
        a = document.getElementById(b + "_selected_bottom");
        a.innerHTML = c.innerHTML
    }
}

function showSortBy(a) {
    showDropDown(a, "categorySortBy")
}

function showColor(a) {
    showDropDown("color_" + a, "color")
}

function disableFormQtyWhereNeeded(a) {
    if (a.id != "addformProduct") {
        a.select("input.disableQty").each(function(f) {
            var b = f.value;
            var g = $("qty_" + b);
            if (g) {
                g.value = "";
                g.disabled = true
            }
            var c = $("addtoregistry_" + b);
            if (c) {
                c.writeAttribute("data-disabled", "true");
                c.addClassName("disabled")
            }
            var d = $("addtocart_" + b);
            if (d) {
                d.disabled = true;
                d.addClassName("disabled")
            }
        })
    }
}

function initAjaxCartForm(e, c, b, a) {
    var d = $(e);
    if (d.initAjaxCartForm) {
        log("initAjaxCartForm for formid: " + e + " already initialized");
        return
    }
    log("initAjaxCartForm for formid: " + e + " and found form: " + d);
    d.observe("click", function(f) {
        var g = f.findElement("input[type=submit]");
        if (g == undefined) {
            return
        }
        d.select("input[type=submit]").each(function(h) {
            if (h != g) {
                h.disabled = true
            }
        })
    });
    disableFormQtyWhereNeeded(d);
    d.observe("submit", function(g) {
        if (g.defaultPrevented) {
            return
        }
        var f = $(e);
        if (f && f._invalid) {
            return
        }
        submitAjaxCartForm(e, false, a);
        f.select("input[type=submit]").each(function(h) {
            h.disabled = false
        });
        if (c) {
            $(c).hide()
        }
        if (b) {
            b()
        }
        Event.stop(g)
    });
    d.initAjaxCartForm = true
}

function onProductFeatureChange(g, d, f) {
    if (!f) {
        f = 1
    }
    var c = $("qty_" + d);
    var e = $("addtocart_" + d);
    var a = $("addtoregistry_" + d);
    if (c) {
        if (g.options.selectedIndex != 0) {
            c.disabled = false;
            if (e) {
                e.disabled = false;
                e.removeClassName("disabled")
            }
            if (a) {
                a.writeAttribute("data-disabled", "false");
                a.removeClassName("disabled")
            }
            var b = c.getValue();
            if (!b || b == "" || b == "0") {
                c.setValue(f)
            }
        } else {
            c.disabled = true;
            if (e) {
                e.disabled = true;
                e.addClassName("disabled")
            }
            if (a) {
                a.writeAttribute("data-disabled", "true");
                a.addClassName("disabled")
            }
        }
    }
    checkFeaturePrice(d)
}

function checkFeaturePrice(c) {
    var g = document.getElementById(c + "_price");
    if (!g) {
        return
    }
    if (typeof priceFeatureMap[c] == "undefined") {
        return
    }
    var f = [];
    for (var a = 0; a < 10; a++) {
        var b = document.getElementById("feature_" + c + "_" + a);
        if (!b) {
            break
        }
        f.push(b.value)
    }
    f = f.sort();
    var e = "";
    for (var a = 0; a < f.length; a++) {
        if (a > 0) {
            e += "_"
        }
        e += f[a]
    }
    var d = priceFeatureMap[c]["_default_"];
    if (typeof priceFeatureMap[c][e] != "undefined") {
        d = priceFeatureMap[c][e]
    }
    g.innerHTML = d
}

function changeCountrySwitchStateProvince(b, d, c) {
    if (!b) {
        return
    }
    var g = b.form[d];
    var e = document.getElementById(d + "_label");
    var a = b.form[c];
    var f = document.getElementById(c + "_label");
    var h = b[b.selectedIndex].value;
    if ("USA" == h) {
        a.style.display = "none";
        f.style.display = "none";
        g.style.display = "";
        e.style.display = ""
    } else {
        a.style.display = "";
        f.style.display = "";
        g.style.display = "none";
        e.style.display = "none";
        g.value = ""
    }
}

function disableButton(a, b) {
    a.removeAttribute("onclick");
    a.disabled = true;
    a.className = a.className + " disabled";
    a.style.cursor = "wait";
    a.value = b
}

function submitAndDisableButton(b, a, c) {
    disableButton(a, c);
    b.submit();
    return false
}

function submitAndDisableAjaxButton(b, a, c) {
    disableButton(a, c);
    submitAjaxCartForm(b);
    return false
}

function replaceSubmitButton(a) {
    var b = document.createElement("input");
    b.type = "button";
    b.id = a.id;
    b.value = a.value;
    b.className = a.className;
    a.parentNode.replaceChild(b, a);
    return b
}

function initSubmitAndDisableButton(b, a, d) {
    var c = replaceSubmitButton(a);
    Event.observe(c, "click", function() {
        submitAndDisableButton(b, c, d)
    })
}

function initSubmitAndDisableAjaxButton(b, a, d) {
    var c = replaceSubmitButton(a);
    Event.observe(c, "click", function() {
        submitAndDisableAjaxButton(b, c, d)
    })
}

function setMetaContents(d, c) {
    var a = document.getElementsByTagName("meta");
    for (var b = 0; b < a.length; b++) {
        if (a[b].getAttribute("property") == d) {
            a[b].content = c
        }
    }
}

function getMetaContent(c) {
    var a = document.getElementsByTagName("meta");
    for (var b = 0; b < a.length; b++) {
        if (a[b].getAttribute("property") == c) {
            return a[b].content
        }
    }
}

function postBuyFB(c, a, b) {
    hidePostBuyFB("postBuy_" + a);
    hidePostBuyFB("userMessage_" + a);
    setMessagePostBuyFB("successMessage_" + a, "Communicating with Facebook...");
    c = "http://www.graciousstyle.com" + c;
    FB.api(b + c, "post", function(d) {
        if (d && !d.error) {
            setMessagePostBuyFB("successMessage_" + a, "Shared on Facebook")
        } else {
            setMessagePostBuyFB("successMessage_" + a, "")
        }
    })
}

function clearMessagesFB(c) {
    var a = 0;
    var b = document.getElementById(c + a);
    while (b) {
        b.innerHTML = "";
        a++;
        b = document.getElementById(c + a)
    }
}

function setMessagePostBuyFB(a, c) {
    var b = document.getElementById(a);
    if (b) {
        b.innerHTML = c
    }
}

function checkLoginStatusAndPostBuyFB(d, b, c) {
    var a = checkLoginStatusFB();
    if (a == "") {
        postBuyFB(d, b, c)
    } else {
        FB.login(function(e) {
            if (e.authResponse) {
                postBuyFB(d, b, c)
            }
        }, {
            scope: "publish_actions"
        })
    }
}

function hidePostBuyFB(b) {
    var a = document.getElementById(b);
    if (a) {
        a.style.display = "none"
    }
}

function createPageUrlAndPostActionFB(d, b, c) {
    var a = document.getElementById("userMessage_" + b);
    if (a) {
        if (a.value != "") {
            d = d + "&message=" + a.value.replace(/ /g, "+")
        }
    }
    checkLoginStatusAndPostBuyFB(d, b, c)
}

function checkLoginStatusFB() {
    var a = "status";
    FB.getLoginStatus(function(b) {
        if (b.status == "connected") {
            a = ""
        } else {
            a = b.status
        }
    });
    return a
}

function getFBUserData() {
    FB.api("/me?access_token=" + this.accessToken, function(a) {
        if (!a.error) {
            if (a.email) {
                saveFacebookUserEmaiL(a.email)
            }
        } else {
            log(a)
        }
    })
}

function doWhenFBLoggedIn(c, b) {
    if (c) {
        var a = checkLoginStatusFB();
        if (a == "") {
            c()
        } else {
            FB.login(function(d) {
                if (d.authResponse) {
                    this.accessToken = FB.getAuthResponse()["accessToken"];
                    getFBUserData();
                    c()
                } else {
                    if (b) {
                        b()
                    }
                }
            }, {
                scope: "publish_actions,email,publish_stream"
            })
        }
    }
}

function loveOnFacebook(a, c, b) {
    if (b && b.length > 0) {
        $("buttonLoveOnFacebook_message").hide();
        $("buttonLoveOnFacebook_loading").show();
        doWhenFBLoggedIn(showLoveOnFacebookPopupWindow.bind(null, a, c, b), function() {
            $("buttonLoveOnFacebook_loading").hide();
            $("buttonLoveOnFacebook_message").show();
            $("buttonLoveOnFacebook_message").update("Unexpected error occurred.")
        })
    } else {
        log("Cannot loveOnFacebook, empty description was given")
    }
}

function showLoveOnFacebookPopupWindow(e, d, g) {
    var a = document.getElementById("popupLoveOnFacebook");
    if (a) {
        removeChildElements(a);
        var c = document.createElement("table");
        c.className = "cartTable";
        var f = document.createElement("tbody");
        var i, h, b;
        i = document.createElement("tr");
        h = document.createElement("th");
        h.setAttribute("align", "left");
        b = document.createElement("textarea");
        b.setAttribute("rows", "4");
        b.setAttribute("cols", "40");
        b.setAttribute("placeholder", "Additional comments");
        b.setAttribute("style", "width:100%;padding:0");
        b.id = "loveOnFacebook_userMessage";
        h.appendChild(b);
        i.appendChild(h);
        f.appendChild(i);
        i = document.createElement("tr");
        h = document.createElement("th");
        h.setAttribute("align", "center");
        h.setAttribute("style", "padding-top:0");
        b = document.createElement("input");
        b.type = "button";
        b.id = "buttonClose";
        b.className = "smallSubmit";
        b.value = "Close";
        b.setAttribute("onclick", "cleanupAndHideElement('popupLoveOnFacebook');$(\"buttonLoveOnFacebook_loading\").hide();");
        h.appendChild(b);
        b = document.createElement("input");
        b.setAttribute("style", "margin-left:4px;");
        b.type = "button";
        b.id = "buttonShare";
        b.className = "smallSubmit";
        b.value = "Love It";
        b.setAttribute("onclick", "doLoveOnFacebook('" + e + "', '" + d + "', '" + g + "')");
        h.appendChild(b);
        i.appendChild(h);
        f.appendChild(i);
        c.appendChild(f);
        a.appendChild(c);
        movePopupToView($("popupLoveOnFacebook"), 10, $("buttonLoveOnFacebook"));
        a.style.display = "block"
    }
}

function doLoveOnFacebook(c, f, e) {
    if (e) {
        cleanupAndHideElement("popupLoveOnFacebook");
        var d = "http://www.graciousstyle.com" + f;
        var b = "/me/" + c + ":love?product=";
        var a = $("loveOnFacebook_userMessage");
        var g = false;
        saveFacebookLoveAction();
        FB.api(b + d, "post", function(h) {
            if (h && !h.error) {
                log("doLoveOnFacebook: Success");
                log(h);
                if (a && a.value != "") {
                    postMessageOnWall(a.value)
                }
                g = true
            } else {
                log(h.error);
                $("buttonLoveOnFacebook_message").update(h.error.message);
                $("buttonLoveOnFacebook_message").show()
            }
            $("buttonLoveOnFacebook_loading").hide();
            if (g) {
                $("buttonLoveOnFacebook").hide();
                $("buttonLoveOnFacebook_message").update("Thank you for sharing!");
                $("buttonLoveOnFacebook_message").show()
            }
        })
    } else {
        log("Cannot loveOnFacebook, empty description was given")
    }
}

function saveFacebookLoveAction() {
    var a = getMetaContent("og:title");
    var b = getMetaContent("og:image");
    if (a && a) {
        saveFacebookAction(window.location.href, "love", b, a)
    }
}

function saveFacebookLike(b) {
    var a = getMetaContent("og:title");
    var c = getMetaContent("og:image");
    if (a && a) {
        saveFacebookAction(b, "like", c, a)
    }
}

function showShareOnFacebookPopup() {
    if (productArray && productArray.length > 0) {
        doWhenFBLoggedIn(showShareOnFacebookPopupWindow)
    } else {
        log("Cannot showShareOnFacebookPopup, empty product array was given")
    }
}

function saveFacebookUserEmaiL(a) {
    if (a) {
        new Ajax.Request("/webstore/control/saveFacebookUserEmailAjax", {
            method: "post",
            parameters: {
                emailAddress: a
            }
        })
    }
}

function showShareOnFacebookPopupWindow() {
    var b = document.getElementById("popupShareOnFacebook");
    if (b) {
        var d = document.createElement("table");
        d.className = "cartTable";
        var e = document.createElement("tbody");
        var j = document.createElement("tr");
        var g = document.createElement("th");
        g.setAttribute("colspan", "3");
        g.setAttribute("align", "left");
        var c = document.createTextNode("Share");
        g.appendChild(c);
        j.appendChild(g);
        e.appendChild(j);
        for (var f = 0; f < productArray.length; f++) {
            createFBProductRow(e, productArray[f], f)
        }
        d.appendChild(e);
        b.appendChild(d);
        var a = document.createElement("div");
        a.setAttribute("style", "float:right; padding-top:6px;");
        c = document.createElement("input");
        c.type = "button";
        c.id = "buttonClose";
        c.className = "smallSubmit";
        c.value = "Close";
        c.setAttribute("onclick", "cleanupAndHideElement('popupShareOnFacebook')");
        a.appendChild(c);
        b.appendChild(a);
        c = document.createElement("input");
        c.setAttribute("style", "margin-left:4px;");
        c.type = "button";
        c.id = "buttonShare";
        c.className = "smallSubmit";
        c.value = "Share on Facebook";
        c.setAttribute("onclick", "shareOnFacebook()");
        a.appendChild(c);
        var h = document.createElement("label");
        h.id = "successMessage";
        h.setAttribute("style", "margin-left:8px;");
        a.appendChild(h);
        b.appendChild(a);
        if (typeof reposition == "undefined" || reposition == true) {
            movePopupToView($("popupShareOnFacebook"), 10, $("buttonShareOnFacebook"))
        }
        b.style.display = "block"
    }
}

function createFBProductRow(c, b, a) {
    row = document.createElement("tr");
    cell = document.createElement("td");
    cell.setAttribute("align", "center");
    el = document.createElement("input");
    el.type = "checkbox";
    el.id = "isShare_" + a;
    el.setAttribute("checked", "checked");
    cell.appendChild(el);
    row.appendChild(cell);
    cell = document.createElement("td");
    cell.setAttribute("width", "72");
    el = document.createElement("img");
    el.setAttribute("src", b.imageUrl);
    el.setAttribute("width", "72");
    el.setAttribute("height", "72");
    el.setAttribute("align", "left");
    cell.appendChild(el);
    row.appendChild(cell);
    cell = document.createElement("td");
    cell.innerHTML = b.name;
    el = document.createElement("br");
    cell.appendChild(el);
    el = document.createElement("textarea");
    el.setAttribute("rows", "2");
    el.setAttribute("cols", "40");
    el.setAttribute("placeholder", "Additional comments");
    el.setAttribute("style", "width:300px");
    el.id = "userMessage_" + a;
    cell.appendChild(el);
    row.appendChild(cell);
    c.appendChild(row)
}

function cleanupAndHideElement(b) {
    var a = document.getElementById(b);
    if (a) {
        a.style.display = "none";
        removeChildElements(a)
    }
}

function removeChildElements(a) {
    if (a && a.hasChildNodes()) {
        while (a.childNodes.length >= 1) {
            a.removeChild(a.firstChild)
        }
    }
}

function shareOnFacebook() {
    if (productArray) {
        for (var e = 0; e < productArray.length; e++) {
            var h = document.getElementById("isShare_" + e);
            if (h && h.checked) {
                var d = "/me/" + fbNamespace + ":" + fbAction + "?" + fbObject + "=";
                var f = productArray[e].productUrl;
                var c = productArray[e].imageUrl;
                var g = productArray[e].name;
                var a = document.getElementById("userMessage_" + e);
                var b = "";
                if (a) {
                    if (a.value != "") {
                        b = a.value
                    }
                }
                shareActionOnFacebook(f, d, b, fbAction, c, g)
            }
        }
    }
    showThanksMessage()
}

function shareActionOnFacebook(e, d, c, a, b, f) {
    e = "http://www.graciousstyle.com" + e;
    saveFacebookAction(e, a, b, f);
    FB.api(d + e, "post", function(g) {
        if (g && !g.error) {
            if (c && c != "") {
                postMessageOnWall(c)
            }
        } else {
            log(g.error)
        }
    })
}

function saveFacebookAction(c, a, b, d) {
    FB.api("/me", function(e) {
        if (!e.error) {
            new Ajax.Request("/webstore/control/saveFacebookActionAjax", {
                method: "post",
                parameters: {
                    fbAction: a,
                    linkToProductPage: c,
                    email: e.email,
                    facebookUserId: e.id,
                    name: e.name,
                    username: e.username,
                    userInfoUrl: e.link,
                    imageUrl: b,
                    productName: d
                }
            })
        } else {
            log(e)
        }
    })
}

function postMessageOnWall(a) {
    FB.api("/me/feed", "post", {
        message: a
    }, function(b) {
        if (!b || b.error) {
            log(b.error)
        } else {}
    })
}

function showThanksMessage() {
    var a = document.getElementById("buttonShare");
    if (a) {
        a.setAttribute("style", "display:none")
    }
    var b = document.getElementById("successMessage");
    if (b) {
        b.innerHTML = "Thank you for sharing!"
    }
}

function showRegistryWidgetPostScreen() {
    var a = document.getElementById("registryWidgetPostScreenPopup");
    if (a) {
        var b = document.getElementById("styleSelector");
        if (b) {
            b.options.selectedIndex = 0;
            getWidgetIncludeCode(b.value)
        }
        movePopupToView(a, 10, $("buttonShowRegistryWidgetPostScreen"));
        a.style.display = "block"
    }
}

function hideRegistryWidgetPostScreen() {
    var a = document.getElementById("registryWidgetPostScreenPopup");
    if (a) {
        a.style.display = "none"
    }
}

function getWidgetIncludeCode(e) {
    var c = document.getElementById("widgetLink");
    var d = document.getElementById("webKey");
    var b = $("shoppingListId");
    var a = '<div id="shoppingListWidget' + b.value + '" class="shoppingListWidget"';
    if (d) {
        a += ' data-shopping-list-id="' + d.value + '"'
    }
    if (e) {
        a += ' data-theme="' + e + '"'
    }
    a += "></div>\n";
    a += '<script type="text/javascript" src="';
    if (c) {
        a += c.value
    }
    a += '"><\/script>';
    var f = document.getElementById("widgetCode");
    if (f) {
        f.value = a
    }
}

function previewRegistryWidgetPostScreen() {
    var e = $("widgetLink");
    var g = $("webKey");
    var f = $("styleSelector");
    var d = $("shoppingListId");
    var b = 950;
    var a = 550;
    var h = "/webstore/control/registryWidgetPreview";
    if (e && g && f) {
        var c = window.open(h + "?widgetLink=" + e.value + "&webKey=" + g.value + "&shoppingListId=" + d.value + "&popupStyle=" + f.value, "FieldLookup", "width=" + b + ",height=" + a + ",scrollbars=yes,status=no,resizable=yes,top=" + (screen.height / 2 - (a / 2)) + ",left=" + (screen.width / 2 - (b / 2)) + ",dependent=yes,alwaysRaised=yes");
        c.opener = window;
        c.focus()
    }
}

function loadQuickView(d, f) {
    if (d) {
        url = "/webstore/control/quickviewPopupProduct";
        rel = "quickviewPopupProduct_" + d
    } else {
        url = "/webstore/control/quickviewPopupCategory";
        rel = "quickviewPopupCategory_" + f
    }
    log("loadQuickView pid: " + d + " cid: " + f);
    var e = rel;
    var a = $(e);
    if (a) {
        document.body.removeChild(a)
    }
    var c = e + "Inner";
    log("loadQuickView pid: " + d + " cid: " + f + " container: " + rel + " not found, creating");
    a = new Element("div", {
        id: e,
        "data-close-on-top": "1",
        "data-css": "lbQuickviewPopup"
    }).hide();
    var b = new Element("div", {
        "class": c
    }).insert(new Element("div", {
        align: "center"
    }).insert(new Element("img", {
        src: "/images/lb_loading.gif"
    })));
    a.appendChild(b);
    document.body.appendChild(a);
    new Ajax.Request(url, {
        method: "get",
        parameters: {
            productId: d,
            productCategoryId: f
        },
        evalJSON: "force",
        onSuccess: function(g) {
            $$("." + c).each(function(h) {
                h.update(g.responseText + '<div class="endBlogPost"></div>')
            })
        }
    })
}

function initThumbnailImg(c) {
    var d = $(c);
    console.log("initThumbnailImg ", c);
    var f = d.readAttribute("data-init");
    if (f) {
        return
    }
    var a, g;
    a = d.readAttribute("data-product-id");
    if (!a) {
        g = d.readAttribute("data-category-id")
    }
    if (a || g) {
        var b;
        if (a) {
            b = "/webstore/control/quickviewPopupProduct?productId=" + a;
            rel = "quickviewPopupProduct_" + a
        } else {
            b = "/webstore/control/quickviewPopupCategory?productCategoryId=" + g;
            rel = "quickviewPopupCategory_" + g
        }
        var e = new Element("a", {
            "class": "quickview",
            href: b,
            rel: "lightbox#" + rel + "#1200"
        }).update("Quick View").hide();
        d.insert(e);
        e.observe("click", function() {
            loadQuickView(a, g)
        });
        d.observe("mouseover", function() {
            e.show()
        });
        d.observe("mouseout", function() {
            e.hide()
        });
        d.writeAttribute("data-init", "1")
    }
}
document.observe("dom:loaded", function() {
    console.log("dom:loaded ...");
    $$(".thumbnailImg").each(function(a) {
        initThumbnailImg(a)
    })
});

function loadJavaScript(a, b) {
    var d = ("https:" == document.location.protocol ? "https" : "http");
    var c = document.createElement("script");
    c.setAttribute("type", "text/javascript");
    c.setAttribute("src", d + a);
    if (b && c.readyState) {
        c.onreadystatechange = function() {
            if (this.readyState == "complete" || this.readyState == "loaded") {
                b()
            }
        }
    } else {
        if (b) {
            c.onload = b
        }
    }(document.getElementsByTagName("head")[0] || document.documentElement).appendChild(c)
}

function _fb_init(opts, fbEvent, eventFunction) {
    if (window.FB) {
        FB.init(opts);
        if (fbEvent && eventFunction) {
            FB.Event.subscribe(fbEvent, function(response) {
                eval(eventFunction)
            })
        }
        return true
    }
    return false
}

function initFacebook(c, b, a) {
    var d = c;
    if (!d) {
        d = {
            status: true,
            cookie: true,
            xfbml: true
        }
    }
    if (!_fb_init(d, b)) {
        loadJavaScript("://connect.facebook.net/en_US/all.js#xfbml=1", function() {
            _fb_init(d, b, a)
        })
    }
}
document.observe("dom:loaded", function() {
    initFacebook();
    loadJavaScript("://apis.google.com/js/plusone.js");
    loadJavaScript("://platform.twitter.com/widgets.js");
    Placeholders.init()
});

function setupAutoTab(a) {
    if (a == null) {
        return
    }
    for (var b = 0; b < a.length; b++) {
        var c = a[b];
        c.nextAutoTabElement = null;
        if (b < (a.length - 1)) {
            c.nextAutoTabElement = a[b + 1]
        }
        c.prevAutoTabElement = null;
        if (b > 0) {
            c.prevAutoTabElement = a[b - 1]
        }
        if (typeof c.placeholder === "undefined") {
            var f = c.getAttribute("placeholder");
            if (f && f.length > 0) {
                c.workaroundPlaceholder = f
            }
        }
        Event.observe(c, "keyup", function d(h) {
            var i = Event.element(h);
            if (i.value.length == i.getAttribute("maxlength") && h.keyCode != 8 && h.keyCode != 16 && h.keyCode != 9 && h.keyCode != 13 && h.keyCode != 37 && h.keyCode != 39) {
                if (i.workaroundPlaceholder) {
                    if (i.value == i.workaroundPlaceholder || i.value.substring(1) == i.workaroundPlaceholder) {
                        return
                    }
                }
                var g = i.nextAutoTabElement;
                if (g) {
                    g.activate()
                }
            }
        });
        Event.observe(c, "keydown", function e(k) {
            var l = Event.element(k);
            if (k.keyCode == 8) {
                var g = false;
                if (typeof l.selectionStart == "number") {
                    g = (l.selectionStart == 0)
                } else {
                    if (document.selection && document.selection.createRange) {
                        var h = document.selection.createRange();
                        if (!h) {
                            return
                        }
                        var j = h.getBookmark();
                        g = (j.charCodeAt(2) == 2)
                    }
                } if (g) {
                    var i = l.prevAutoTabElement;
                    if (i) {
                        i.focus()
                    }
                }
            }
        })
    }
}

function sideMenuToggle(a) {
    if (!a || a.length == 0) {
        return
    }
    var b = false;
    $$(".categoryList .open").each(function(c) {
        c.toggleClassName("open");
        c.toggleClassName("closed");
        if (!b && c.hasClassName(a)) {
            b = true
        }
    });
    if (!b) {
        $$(".categoryList ." + a).each(function(c) {
            if (c.hasClassName("closed")) {
                c.toggleClassName("closed");
                c.toggleClassName("open")
            }
        })
    }
}
var MyProductCompleter = Class.create(Ajax.Autocompleter, {
    initialize: function($super, d, c, b, a) {
        $super(d, c, b, a)
    },
    onComplete: function(a) {
        var b = a.responseText;
        if (b.isJSON()) {
            this.handleJSON(b.evalJSON())
        }
    },
    updateChoices: function(c) {
        if (!this.changed && this.hasFocus) {
            this.update.innerHTML = c;
            Element.cleanWhitespace(this.update);
            Element.cleanWhitespace(this.update.down());
            if (this.update.firstChild && this.update.down().childNodes) {
                this.entryCount = this.update.down().childNodes.length;
                for (var a = 0; a < this.entryCount; a++) {
                    var b = this.getEntry(a);
                    b.autocompleteIndex = a;
                    this.addObservers(b)
                }
            } else {
                this.entryCount = 0
            }
            this.stopIndicator();
            this.index = -1;
            if (this.entryCount == 1 && this.options.autoSelect) {
                this.selectEntry();
                this.hide()
            } else {
                this.render()
            }
        }
    },
    handleJSON: function(a) {
        var b = "<ul>";
        if (a.options) {
            a.options.each(function(c) {
                b += "<li>";
                if (c.payload && c.payload.url) {
                    b += '<a href="' + c.payload.url + '">'
                }
                b += c.text;
                if (c.payload && c.payload.url) {
                    b += "</a>"
                }
                b += "</li>"
            })
        } else {
            if (a.length > 0) {
                a.each(function(c) {
                    b += "<li>";
                    b += c.keyword;
                    b += "</li>"
                })
            }
        }
        b += "</ul>";
        this.updateChoices(b)
    }
});

function setupScrollToTopWidget(a, c, b) {
    Event.observe($(window), "scroll", function(f) {
        var d = document.viewport.getScrollOffsets().top;
        if (!a) {
            a = document.viewport.getHeight()
        }
        if (d > a) {
            $(c).show()
        } else {
            $(c).hide()
        }
    });
    $(c).observe("click", function(d) {
        Effect.ScrollTo(b)
    })
}

function toggle(a) {
    a.checked = !a.checked
}

function checkToggleDefault(a) {
    checkToggle(a, "selectAllForm")
}

function checkToggle(h, f) {
    var g = document[f];
    if (h.checked) {
        var a = g.elements.length;
        var d = true;
        for (var c = 0; c < a; c++) {
            var b = g.elements[c];
            if (b.name.substring(0, 10) == "_rowSubmit" && !b.checked) {
                d = false
            }
            g.selectAll.checked = d
        }
    } else {
        g.selectAll.checked = false
    }
}

function toggleAllDefault(a) {
    toggleAll(a, "selectAllForm")
}

function toggleAll(g, d) {
    var f = document[d];
    var a = f.elements.length;
    for (var c = 0; c < a; c++) {
        var b = f.elements[c];
        if (b.name.substring(0, 10) == "_rowSubmit" && b.checked != g.checked) {
            toggle(b)
        }
    }
}

function selectAllDefault() {
    selectAll("selectAllForm")
}

function selectAll(d) {
    var e = document[d];
    var a = e.elements.length;
    for (var c = 0; c < a; c++) {
        var b = e.elements[c];
        if ((b.name == "selectAll" || b.name.substring(0, 10) == "_rowSubmit") && !b.checked) {
            toggle(b)
        }
    }
}

function removeSelectedDefault() {
    removeSelected("selectAllForm")
}

function removeSelected(a) {
    var b = document[a];
    b.removeSelected.value = true;
    b.submit()
}

function highlightRow(c, b) {
    var a = document.getElementById(b).className;
    if (c.checked) {
        if (a == "") {
            document.getElementById(b).className = "selected"
        } else {
            if (a == "alternate-row") {
                document.getElementById(b).className = "alternate-rowSelected"
            }
        }
    } else {
        if (a == "selected") {
            document.getElementById(b).className = ""
        } else {
            if (a == "alternate-rowSelected") {
                document.getElementById(b).className = "alternate-row"
            }
        }
    }
}

function highlightAllRows(h, b, f) {
    var g = document[f];
    var a = g.elements.length;
    for (var d = 0; d < a; d++) {
        var c = g.elements[d];
        if (c.name.substring(0, 10) == "_rowSubmit") {
            highlightRow(h, b + c.name.substring(13))
        }
    }
}

function popUp(c, b, a, d) {
    popupWindow = window.open(c, b, "location=no,scrollbars,width=" + d + ",height=" + a)
}

function popUpSmall(b, a) {
    popUp(b, a, "300", "450")
}

function popUpPrint(b, a) {
    popUpPrint(b, a, null, null)
}

function popUpPrint(b, a, c) {
    popUpPrint(b, a, c, null)
}

function popUpPrint(b, a, d, c) {
    if (b == null) {
        b = "http://localhost:10080/"
    }
    if (a != null) {
        a = a.replace(/\:/g, "%3A");
        a = a.replace(/\//g, "%2F");
        a = a.replace(/\#/g, "%23");
        a = a.replace(/\?/g, "%3F");
        a = a.replace(/\=/g, "%3D");
        url = b + a;
        window.open(url, "screen1", "location=no,statusbar=1,menubar=0,scrollbars,width=60,height=10,top=0,left=0");
        self.focus();
        if (d != null) {
            d = d.replace(/\:/g, "%3A");
            d = d.replace(/\//g, "%2F");
            d = d.replace(/\#/g, "%23");
            d = d.replace(/\?/g, "%3F");
            d = d.replace(/\=/g, "%3D");
            url = b + d;
            window.open(url, "screen2", "location=no,statusbar=1,menubar=0,scrollbars,width=60,height=10,top=0,left=0");
            self.focus();
            if (c != null) {
                c = c.replace(/\:/g, "%3A");
                c = c.replace(/\//g, "%2F");
                c = c.replace(/\#/g, "%23");
                c = c.replace(/\?/g, "%3F");
                c = c.replace(/\=/g, "%3D");
                url = b + c;
                window.open(url, "screen13", "location=no,statusbar=1,menubar=0,scrollbars,width=60,height=10,top=0,left=0");
                self.focus()
            }
        }
    }
}

function getStyleObject(a) {
    if (document.getElementById && document.getElementById(a)) {
        return document.getElementById(a).style
    } else {
        if (document.all && document.all(a)) {
            return document.all(a).style
        } else {
            if (document.layers && document.layers[a]) {
                return document.layers[a]
            } else {
                return false
            }
        }
    }
}

function changeObjectVisibility(a, c) {
    var b = getStyleObject(a);
    if (b) {
        b.visibility = c;
        return true
    } else {
        return false
    }
}

function confirmActionLink(c, b) {
    if (c == null) {
        c = "Are you sure you want to do this?"
    }
    var a = confirm(c);
    if (a) {
        if (b != null) {
            location.replace(b)
        }
    }
}

function confirmActionFormLink(c, a) {
    if (c == null) {
        c = "Are you sure you want to do this?"
    }
    var b = confirm(c);
    if (b) {
        if (a != null) {
            document.forms[a].submit()
        }
    }
}

function ajaxUpdateArea(c, a, b) {
    new Ajax.Updater(c, a, {
        parameters: b
    })
}

function ajaxUpdateAreas(a) {
    responseFunction = function(e) {};
    var d = a.split(",");
    var c = parseInt(d.length / 3);
    for (var b = 0; b < c * 3; b = b + 3) {
        new Ajax.Updater(d[b], d[b + 1], {
            parameters: d[b + 2],
            onComplete: responseFunction,
            evalScripts: true
        })
    }
}

function ajaxUpdateAreaPeriodic(d, b, c, a) {
    new Ajax.PeriodicalUpdater(d, b, {
        parameters: c,
        frequency: a
    })
}

function ajaxSubmitRequestUpdateAreas(b, c, a) {
    updateFunction = function(d) {
        ajaxUpdateAreas(a)
    };
    new Ajax.Request(b, {
        parameters: c,
        onComplete: updateFunction
    })
}

function submitFormInBackground(a, b, c) {
    submitFormDisableSubmits(a);
    updateFunction = function() {
        new Ajax.Updater(b, c)
    };
    new Ajax.Request(a.action, {
        parameters: a.serialize(true),
        onComplete: updateFunction
    })
}

function ajaxSubmitFormUpdateAreas(b, a) {
    submitFormDisableSubmits($(b));
    updateFunction = function(d) {
        var c = d.responseText.evalJSON(true);
        if (c._ERROR_MESSAGE_LIST_ != undefined || c._ERROR_MESSAGE_ != undefined) {
            if (!$("content-messages")) {
                if ($("app-navigation")) {
                    $("app-navigation").insert({
                        after: '<div id="content-messages"></div>'
                    })
                }
            }
            $("content-messages").addClassName("errorMessage");
            $("content-messages").update(c._ERROR_MESSAGE_LIST_ + " " + c._ERROR_MESSAGE_);
            new Effect.Appear("content-messages", {
                duration: 0.5
            })
        } else {
            if ($("content-messages")) {
                $("content-messages").removeClassName("errorMessage");
                new Effect.Fade("content-messages", {
                    duration: 0
                })
            }
            ajaxUpdateAreas(a)
        }
    };
    new Ajax.Request($(b).action, {
        parameters: $(b).serialize(true),
        onComplete: updateFunction
    })
}

function ajaxAutoCompleter(a) {
    var e = a.split(",");
    var c = parseInt(e.length / 3);
    for (var b = 0; b < c * 3; b = b + 3) {
        var d = e[b] + "_autoCompleterOptions";
        $(e[b]).insert({
            after: '<div class="autocomplete"id=' + d + "></div>"
        });
        new Ajax.Autocompleter($(e[b]), d, e[b + 1], {
            parameters: e[b + 2]
        })
    }
}

function ajaxAutoCompleteDropDown(e, d, c, a) {
    var f = d + "_autoCompleterOptions";
    $(e).insert({
        after: '<div class="autocomplete"id=' + f + "></div>"
    });
    new Autocompleter.Local($(e), f, $H(c), {
        autoSelect: a.autoSelect,
        frequency: a.frequency,
        minChars: a.minChars,
        choices: a.choices,
        partialSearch: a.partialSearch,
        partialChars: a.partialChars,
        ignoreCase: a.ignoreCase,
        fullSearch: a.fullSearch,
        afterUpdateElement: b
    });

    function b(h, g) {
        $(d).value = g.id
    }
}

function toggleCollapsiblePanel(d, f, b, c) {
    var a = $(f);
    var e = $(d).up("li");
    if (a.visible()) {
        e.removeClassName("expanded");
        e.addClassName("collapsed");
        d.title = b
    } else {
        e.removeClassName("collapsed");
        e.addClassName("expanded");
        d.title = c
    }
    Effect.toggle(a, "appear")
}

function toggleScreenlet(g, i, f, c) {
    toggleCollapsiblePanel(g, i, f, c);
    var a = $(i);
    var h = a.up("div");
    if (a.visible()) {
        var d = h.id + "_collapsed=false";
        var e = h.id + "_collapsed=true"
    } else {
        var d = h.id + "_collapsed=true";
        var e = h.id + "_collapsed=false"
    }
    var b = $$("div.nav-pager");
    b.each(function(l) {
        if (l) {
            var k = l.getElementsByTagName("a");
            for (var j = 0; j < k.length; j++) {
                if (k[j].href.indexOf("http") == 0) {
                    k[j].href = replaceQueryParam(k[j].href, d, e)
                }
            }
            k = l.getElementsByTagName("select");
            for (j = 0; j < k.length; j++) {
                if (k[j].href.indexOf("location.href") >= 0) {
                    Element.extend(k[j]);
                    k[j].writeAttribute("onchange", replaceQueryParam(k[j].readAttribute("onchange"), d, e))
                }
            }
        }
    })
}

function ajaxInPlaceEditDisplayField(c, b, a) {
    new Ajax.InPlaceEditor($(c), b, a)
}

function replaceQueryParam(d, b, c) {
    var a = d.replace(b, c);
    if (a.indexOf(c) < 0) {
        if (a.indexOf("?") < 0) {
            a = a + "?" + c
        } else {
            if (a.endsWith("#")) {
                a = a.replace("#", "&" + c + "#")
            } else {
                if (a.endsWith(";")) {
                    a = a.replace(";", " + '&" + c + "';")
                } else {
                    a = a + "&" + c
                }
            }
        }
    }
    return a
}

function submitFormDisableSubmits(e) {
    for (var d = 0; d < e.length; d++) {
        var a = e.elements[d];
        if (a.type == "submit") {
            submitFormDisableButton(a);
            var c = e.name;
            var g = a.name;
            var f = "submitFormEnableButtonByName('" + c + "', '" + g + "')";
            var b = setTimeout(f, 1500)
        }
    }
}

function submitFormDisableButton(a) {
    if (a.form.action != null && a.form.action.length > 0) {
        a.disabled = true
    }
    a.className = a.className + " disabled";
    a.value = a.value + "*"
}

function submitFormEnableButtonByName(c, a) {
    var d = document[c];
    var b = d.elements[a];
    submitFormEnableButton(b)
}

function submitFormEnableButton(a) {
    a.disabled = false;
    a.className = a.className.substring(0, a.className.length - " disabled".length);
    a.value = a.value.substring(0, a.value.length - 1)
}

function expandAll(b) {
    var f, e, d, c, a, g;
    f = document.getElementsByTagName("div");
    for (d = 0; d < f.length; d++) {
        if (/fieldgroup$/.test(f[d].className)) {
            a = f[d].getElementsByTagName("a");
            if (a.length > 0) {
                e = f[d].getElementsByTagName("div");
                for (c = 0; c < e.length; c++) {
                    if (/fieldgroup-body/.test(e[c].className)) {
                        g = e[c]
                    }
                }
                if (g.visible() != b) {
                    toggleCollapsiblePanel(a[0], g.id, "expand", "collapse")
                }
            }
        }
    }
}
var NUM_CENTYEAR = 30;
var BUL_TIMECOMPONENT = false;
var BUL_YEARSCROLL = true;
var calendars = [];
var lookups = [];
var RE_NUM = /^\-?\d+$/;
var webPath = "";
var NS4 = (navigator.appName.indexOf("Netscape") >= 0 && !document.getElementById) ? true : false;
var IE4 = (document.all && !document.getElementById) ? true : false;
var IE5 = (document.getElementById && document.all) ? true : false;
var NS6 = (document.getElementById && navigator.appName.indexOf("Netscape") >= 0) ? true : false;
var mx, my;

function moveobj(a) {
    if (NS4 || NS6) {
        mx = a.screenX;
        my = a.screenY
    } else {
        if (IE5 || IE4) {
            mx = event.screenX;
            my = event.screenY
        }
    }
}
if (NS4) {
    document.captureEvents(Event.MOUSEMOVE)
}
document.onmousemove = moveobj;

function call_cal(b, c) {
    var a = new calendar1(b);
    a.year_scroll = true;
    a.time_comp = true;
    a.popup(c)
}

function call_cal_notime(b, c) {
    var a = new calendar1(b);
    a.year_scroll = true;
    a.time_comp = false;
    a.popup(c)
}

function calendar1(a) {
    this.gen_date = cal_gen_date1;
    this.gen_time = cal_gen_time1;
    this.gen_tsmp = cal_gen_tsmp1;
    this.prs_date = cal_prs_date1;
    this.prs_time = cal_prs_time1;
    this.prs_tsmp = cal_prs_tsmp1;
    this.popup = cal_popup1;
    if (!a) {
        return cal_error("Error calling the calendar: no target control specified")
    }
    if (a.value == null) {
        return cal_error("Error calling the calendar: parameter specified is not valid tardet control")
    }
    this.target = a;
    this.time_comp = BUL_TIMECOMPONENT;
    this.year_scroll = BUL_YEARSCROLL;
    this.id = calendars.length;
    calendars[this.id] = this
}

function cal_popup1(b) {
    this.dt_current = this.prs_tsmp(b ? b : this.target.value);
    if (!this.dt_current) {
        return
    }
    var a = window.open("/images/calendar.html?datetime=" + this.dt_current.valueOf() + "&id=" + this.id, "Calendar", "width=150,height=" + (this.time_comp ? 220 : 235) + ",status=no,resizable=yes,top=" + my + ",left=" + mx + ",dependent=yes,alwaysRaised=yes");
    a.opener = window;
    a.focus()
}

function cal_gen_tsmp1(a) {
    return (this.gen_date(a) + " " + this.gen_time(a))
}

function cal_gen_date1(a) {
    return (a.getFullYear() + "-" + (a.getMonth() < 9 ? "0" : "") + (a.getMonth() + 1) + "-" + (a.getDate() < 10 ? "0" : "") + a.getDate())
}

function cal_gen_time1(a) {
    return ((a.getHours() < 10 ? "0" : "") + a.getHours() + ":" + (a.getMinutes() < 10 ? "0" : "") + (a.getMinutes()) + ":" + (a.getSeconds() < 10 ? "0" : "") + (a.getSeconds()) + "." + (a.getMilliseconds()))
}

function cal_prs_tsmp1(b) {
    if (!b) {
        return (new Date())
    }
    if (RE_NUM.exec(b)) {
        return new Date(b)
    }
    var a = b.split(" ");
    return this.prs_time(a[1], this.prs_date(a[0]))
}

function cal_prs_date1(c) {
    var d = c.split("-");
    if (d.length != 3) {
        return cal_error("Invalid date format: '" + c + "'.\nFormat accepted is dd-mm-yyyy.")
    }
    if (!d[2]) {
        return cal_error("Invalid date format: '" + c + "'.\nNo day of month value can be found.")
    }
    if (!RE_NUM.exec(d[2])) {
        return cal_error("Invalid day of month value: '" + d[2] + "'.\nAllowed values are unsigned integers.")
    }
    if (!d[1]) {
        return cal_error("Invalid date format: '" + c + "'.\nNo month value can be found.")
    }
    if (!RE_NUM.exec(d[1])) {
        return cal_error("Invalid month value: '" + d[1] + "'.\nAllowed values are unsigned integers.")
    }
    if (!d[0]) {
        return cal_error("Invalid date format: '" + c + "'.\nNo year value can be found.")
    }
    if (!RE_NUM.exec(d[0])) {
        return cal_error("Invalid year value: '" + d[0] + "'.\nAllowed values are unsigned integers.")
    }
    var b = new Date();
    b.setDate(1);
    if (d[1] < 1 || d[1] > 12) {
        return cal_error("Invalid month value: '" + d[1] + "'.\nAllowed range is 01-12.")
    }
    b.setMonth(d[1] - 1);
    if (d[0] < 100) {
        d[2] = Number(d[0]) + (d[0] < NUM_CENTYEAR ? 2000 : 1900)
    }
    b.setFullYear(d[0]);
    var a = new Date(d[0], d[1], 0);
    b.setDate(d[2]);
    if (b.getMonth() != (d[1] - 1)) {
        return cal_error("Invalid day of month value: '" + d[2] + "'.\nAllowed range is 01-" + a.getDate() + ".")
    }
    return (b)
}

function cal_prs_time1(a, c) {
    if (!c) {
        return null
    }
    var b = String(a ? a : "").split(":");
    if (!b[0]) {
        c.setHours(0)
    } else {
        if (RE_NUM.exec(b[0])) {
            if (b[0] < 24) {
                c.setHours(b[0])
            } else {
                return cal_error("Invalid hours value: '" + b[0] + "'.\nAllowed range is 00-23.")
            }
        } else {
            return cal_error("Invalid hours value: '" + b[0] + "'.\nAllowed values are unsigned integers.")
        }
    } if (!b[1]) {
        c.setMinutes(0)
    } else {
        if (RE_NUM.exec(b[1])) {
            if (b[1] < 60) {
                c.setMinutes(b[1])
            } else {
                return cal_error("Invalid minutes value: '" + b[1] + "'.\nAllowed range is 00-59.")
            }
        } else {
            return cal_error("Invalid minutes value: '" + b[1] + "'.\nAllowed values are unsigned integers.")
        }
    }
    var d = String(b[2] ? b[2] : "").split(".");
    if (!d[0]) {
        c.setSeconds(0)
    } else {
        if (RE_NUM.exec(d[0])) {
            if (d[0] < 60) {
                c.setSeconds(d[0])
            } else {
                return cal_error("Invalid seconds value: '" + d[0] + "'.\nAllowed range is 00-59.")
            }
        } else {
            return cal_error("Invalid seconds value: '" + d[0] + "'.\nAllowed values are unsigned integers.")
        }
    } if (!d[1]) {
        c.setMilliseconds(0)
    } else {
        if (RE_NUM.exec(d[1])) {
            if (d[1] < 1000) {
                c.setMilliseconds(d[1])
            } else {
                return cal_error("Invalid milliseconds valus: '" + d[1] + "'.\nAllowed range is 00-999.")
            }
        } else {
            return cal_error("Invalid milliseconds value: '" + d[1] + "'.\nAllowed values are unsigned integers.")
        }
    }
    return c
}

function cal_error(a) {
    alert(a);
    return null
}
Carousel = Class.create(Abstract, {
    initialize: function(a, d, b, c) {
        this.scrolling = false;
        this.scroller = $(a);
        this.slides = d;
        if (typeof d === "string") {
            this.slides = $$(d);
            this.slidesSelector = d
        }
        this.controls = b;
        this.options = Object.extend({
            duration: 1,
            auto: false,
            frequency: 3,
            visibleSlides: 1,
            controlClassName: "carousel-control",
            jumperClassName: "carousel-jumper",
            disabledClassName: "carousel-disabled",
            selectedClassName: "carousel-selected",
            circular: false,
            wheel: true,
            effect: "scroll",
            transition: "sinoidal"
        }, c || {});
        if (this.options.effect == "fade") {
            this.options.circular = true
        }
        this.slides.each(function(f, g) {
            f._index = g
        });
        if (this.controls) {
            this.controls.invoke("observe", "click", this.click.bind(this))
        }
        if (this.options.wheel) {
            this.scroller.observe("mousewheel", this.wheel.bindAsEventListener(this)).observe("DOMMouseScroll", this.wheel.bindAsEventListener(this))
        }
        if (this.options.auto) {
            this.start()
        }
        if (this.options.initial) {
            var e = this.slides.indexOf($(this.options.initial));
            if (e > (this.options.visibleSlides - 1) && this.options.visibleSlides > 1) {
                if (e > this.slides.length - (this.options.visibleSlides + 1)) {
                    e = this.slides.length - this.options.visibleSlides
                }
            }
            this.moveTo(this.slides[e])
        }
    },
    click: function(event) {
        this.stop();
        var element = event.findElement("a");
        if (!element.hasClassName(this.options.disabledClassName)) {
            if (element.hasClassName(this.options.controlClassName)) {
                eval("this." + element.rel + "()")
            } else {
                if (element.hasClassName(this.options.jumperClassName)) {
                    this.moveTo(element.rel);
                    if (this.options.selectedClassName) {
                        this.controls.invoke("removeClassName", this.options.selectedClassName);
                        element.addClassName(this.options.selectedClassName)
                    }
                }
            }
        }
        this.deactivateControls();
        event.stop()
    },
    autoLoadSlideIfNeeded: function(a) {
        var c = a.readAttribute("data-loading");
        var b = a.readAttribute("data-url");
        if (b && !c) {
            a.setAttribute("data-loading", "true");
            new Ajax.Request(b, {
                method: "get",
                onSuccess: (function(e) {
                    var d = 0;
                    if (this.current) {
                        d = this.current._index
                    }
                    a.removeAttribute("data-url");
                    a.removeAttribute("data-loading");
                    a.replace(e.responseText);
                    if (this.slidesSelector) {
                        this.slides = $$(this.slidesSelector);
                        this.slides.each(function(g, f) {
                            g._index = f;
                            if (d == f) {
                                this.current = g
                            }
                        })
                    }
                    if (this.controls) {
                        this.activateControls()
                    }
                }).bind(this),
                onFailure: (function(d) {
                    a.update("Error");
                    a.removeAttribute("data-loading")
                }).bind(this)
            })
        }
    },
    moveTo: function(b) {
        if (this.options.beforeMove && (typeof this.options.beforeMove == "function")) {
            this.options.beforeMove()
        }
        this.previous = this.current ? this.current : this.slides[0];
        this.current = $(b);
        this.autoLoadSlideIfNeeded(this.current);
        var c = this.scroller.cumulativeOffset();
        var a = this.current.cumulativeOffset();
        if (this.scrolling) {
            this.scrolling.cancel()
        }
        switch (this.options.effect) {
            case "fade":
                this.scrolling = new Effect.Opacity(this.scroller, {
                    from: 1,
                    to: 0,
                    duration: this.options.duration,
                    afterFinish: (function() {
                        this.scroller.scrollLeft = a[0] - c[0];
                        this.scroller.scrollTop = a[1] - c[1];
                        new Effect.Opacity(this.scroller, {
                            from: 0,
                            to: 1,
                            duration: this.options.duration,
                            afterFinish: (function() {
                                if (this.controls) {
                                    this.activateControls()
                                }
                                if (this.options.afterMove && (typeof this.options.afterMove == "function")) {
                                    this.options.afterMove()
                                }
                            }).bind(this)
                        })
                    }).bind(this)
                });
                break;
            case "scroll":
            default:
                var d;
                switch (this.options.transition) {
                    case "spring":
                        d = Effect.Transitions.spring;
                        break;
                    case "sinoidal":
                    default:
                        d = Effect.Transitions.sinoidal;
                        break
                }
                this.scrolling = new Effect.SmoothScroll(this.scroller, {
                    duration: this.options.duration,
                    x: (a[0] - c[0]),
                    y: (a[1] - c[1]),
                    transition: d,
                    afterFinish: (function() {
                        if (this.controls) {
                            this.activateControls()
                        }
                        if (this.options.afterMove && (typeof this.options.afterMove == "function")) {
                            this.options.afterMove()
                        }
                        this.scrolling = false
                    }).bind(this)
                });
                break
        }
        return false
    },
    prev: function() {
        if (this.current) {
            var a = this.current._index;
            var b = (a == 0) ? (this.options.circular ? this.slides.length - 1 : 0) : a - 1
        } else {
            var b = (this.options.circular ? this.slides.length - 1 : 0)
        } if (b == (this.slides.length - 1) && this.options.circular && this.options.effect != "fade") {
            this.scroller.scrollLeft = (this.slides.length - 1) * this.slides.first().getWidth();
            this.scroller.scrollTop = (this.slides.length - 1) * this.slides.first().getHeight();
            b = this.slides.length - 2
        }
        this.moveTo(this.slides[b])
    },
    next: function() {
        if (this.current) {
            var b = this.current._index;
            var a = (this.slides.length - 1 == b) ? (this.options.circular ? 0 : b) : b + 1
        } else {
            var a = 1
        } if (a == 0 && this.options.circular && this.options.effect != "fade") {
            this.scroller.scrollLeft = 0;
            this.scroller.scrollTop = 0;
            a = 1
        }
        if (a > this.slides.length - (this.options.visibleSlides + 1)) {
            a = this.slides.length - this.options.visibleSlides
        }
        this.moveTo(this.slides[a])
    },
    first: function() {
        this.moveTo(this.slides[0])
    },
    last: function() {
        this.moveTo(this.slides[this.slides.length - 1])
    },
    toggle: function() {
        if (this.previous) {
            this.moveTo(this.slides[this.previous._index])
        } else {
            return false
        }
    },
    stop: function() {
        if (this.timer) {
            clearTimeout(this.timer)
        }
    },
    start: function() {
        this.periodicallyUpdate()
    },
    pause: function() {
        this.stop();
        this.activateControls()
    },
    resume: function(a) {
        if (a) {
            var b = a.relatedTarget || a.toElement;
            if (!b || (!this.slides.include(b) && !this.slides.any(function(c) {
                return b.descendantOf(c)
            }))) {
                this.start()
            }
        } else {
            this.start()
        }
    },
    periodicallyUpdate: function() {
        if (this.timer != null) {
            clearTimeout(this.timer);
            this.next()
        }
        this.timer = setTimeout(this.periodicallyUpdate.bind(this), this.options.frequency * 1000)
    },
    wheel: function(a) {
        a.cancelBubble = true;
        a.stop();
        var b = 0;
        if (!a) {
            a = window.event
        }
        if (a.wheelDelta) {
            b = a.wheelDelta / 120
        } else {
            if (a.detail) {
                b = -a.detail / 3
            }
        } if (!this.scrolling) {
            this.deactivateControls();
            if (b > 0) {
                this.prev()
            } else {
                this.next()
            }
        }
        return Math.round(b)
    },
    isAtFirst: function() {
        return this.current._index == 0
    },
    isAtLast: function() {
        return this.current._index == (this.slides.length - 1)
    },
    deactivateControls: function() {
        this.controls.invoke("addClassName", this.options.disabledClassName)
    },
    activateControls: function() {
        if (this.isAtFirst()) {
            this.controls.invoke("addClassName", "first")
        } else {
            this.controls.invoke("removeClassName", "first")
        } if (this.isAtLast()) {
            this.controls.invoke("addClassName", "last")
        } else {
            this.controls.invoke("removeClassName", "last")
        }
        this.controls.invoke("removeClassName", this.options.disabledClassName)
    }
});
Effect.SmoothScroll = Class.create();
Object.extend(Object.extend(Effect.SmoothScroll.prototype, Effect.Base.prototype), {
    initialize: function(b) {
        this.element = $(b);
        var a = Object.extend({
            x: 0,
            y: 0,
            mode: "absolute"
        }, arguments[1] || {});
        this.start(a)
    },
    setup: function() {
        if (this.options.continuous && !this.element._ext) {
            this.element.cleanWhitespace();
            this.element._ext = true;
            this.element.appendChild(this.element.firstChild)
        }
        this.originalLeft = this.element.scrollLeft;
        this.originalTop = this.element.scrollTop;
        if (this.options.mode == "absolute") {
            this.options.x -= this.originalLeft;
            this.options.y -= this.originalTop
        }
    },
    update: function(a) {
        this.element.scrollLeft = this.options.x * a + this.originalLeft;
        this.element.scrollTop = this.options.y * a + this.originalTop
    }
});
if (typeof(Prototype) == "undefined") {
    throw "Control.Tabs requires Prototype to be loaded."
}
Control.Tabs = Class.create({
    initialize: function(d, b) {
        if (!$(d)) {
            throw "Control.Tabs could not find the element: " + d
        }
        this.activeContainer = false;
        this.activeLink = false;
        this.containers = $H({});
        this.links = [];
        this.options = {
            hover: false,
            tracked: true,
            linkSelector: "li a",
            linkAttribute: "href",
            setClassOnContainer: false,
            activeClassName: "active",
            disabledClassName: "disabled",
            defaultTab: "first",
            autoLinkExternal: true,
            targetRegExp: /#(.+)$/,
            showFunction: Element.show,
            hideFunction: Element.hide
        };
        Object.extend(this.options, b || {});
        if (this.options.tracked) {
            Control.Tabs.instances.push(this)
        }
        var c;
        switch (this.options.linkAttribute) {
            case "href":
            case "src":
                c = function(e) {
                    return (/^#/).test(e.getAttribute(this.options.linkAttribute).replace(window.location.href.split("#")[0], ""))
                };
                break;
            default:
                if (typeof(this.options.linkAttribute) == "function") {
                    c = this.options.linkAttribute
                } else {
                    c = function(e) {
                        return e.hasAttribute(this.options.linkAttribute)
                    }
                }
        }(typeof(this.options.linkSelector) == "string" ? $(d).select(this.options.linkSelector) : this.options.linkSelector($(d))).findAll(c.bind(this)).each(function(e) {
            this.addTab(e)
        }.bind(this));
        this.containers.values().each(Element.hide);
        if (this.options.defaultTab == "first") {
            this.setActiveTab(this.links.first())
        } else {
            if (this.options.defaultTab == "last") {
                this.setActiveTab(this.links.last())
            } else {
                this.setActiveTab(this.options.defaultTab)
            }
        }
        var a = this.options.targetRegExp.exec(window.location);
        if (a && a[1]) {
            a[1].split(",").each(function(e) {
                this.setActiveTab(this.links.find(function(f) {
                    return f.key == e
                }))
            }.bind(this))
        }
        if (this.options.autoLinkExternal) {
            $A(document.getElementsByTagName("a")).each(function(e) {
                if (!this.links.include(e)) {
                    var f = e.href.replace(window.location.href.split("#")[0], "");
                    if (f.substring(0, 1) == "#") {
                        if (this.containers.keys().include(f.substring(1))) {
                            $(e).observe("click", function(h, g) {
                                this.setActiveTab(g.substring(1))
                            }.bindAsEventListener(this, f))
                        }
                    }
                }
            }.bind(this))
        }
    },
    addTab: function(b) {
        this.links.push(b);
        switch (this.options.linkAttribute) {
            case "href":
            case "src":
                b.key = b.getAttribute(this.options.linkAttribute).replace(window.location.href.split("#")[0], "").split("#").last().replace(/#/, "");
                break;
            default:
                if (typeof(this.options.linkAttribute) == "function") {
                    b.key = this.options.linkAttribute(b)
                } else {
                    b.key = b.getAttribute(this.options.linkAttribute)
                }
        }
        var a = this.options.tabs_container ? this.options.tabs_container.down("#" + b.key) : $(b.key);
        if (!a) {
            throw "Control.Tabs: #" + b.key + " was not found on the page."
        }
        this.containers.set(b.key, a);
        b[this.options.hover ? "onmouseover" : "onclick"] = function(c) {
            if (window.event) {
                Event.stop(window.event)
            }
            this.setActiveTab(c);
            return false
        }.bind(this, b)
    },
    getTab: function(a) {
        if (!a && typeof(a) == "undefined") {
            return null
        }
        if (typeof(a) == "string") {
            return this.getTab(this.links.find(function(b) {
                return b.key == a
            }))
        } else {
            if (typeof(a) == "number") {
                return this.getTab(this.links[a])
            } else {
                return this.containers.get(a.key)
            }
        }
    },
    setActiveTab: function(b) {
        if (!b && typeof(b) == "undefined") {
            return
        }
        if (typeof(b) == "string") {
            this.setActiveTab(this.links.find(function(c) {
                return c.key == b
            }))
        } else {
            if (typeof(b) == "number") {
                this.setActiveTab(this.links[b])
            } else {
                if (!(this.options.setClassOnContainer ? $(b.parentNode) : b).hasClassName(this.options.disabledClassName)) {
                    if (b == this.activeLink) {
                        return
                    }
                    if (this.activeContainer) {
                        this.options.hideFunction(this.activeContainer)
                    }
                    this.links.each(function(c) {
                        (this.options.setClassOnContainer ? $(c.parentNode) : c).removeClassName(this.options.activeClassName)
                    }.bind(this));
                    (this.options.setClassOnContainer ? $(b.parentNode) : b).addClassName(this.options.activeClassName);
                    var a = this.containers.get(b.key);
                    this.activeContainer = a;
                    this.activeLink = b;
                    this.options.showFunction(a);
                    if (a.onShow) {
                        a.onShow()
                    }
                }
            }
        }
    },
    disableTab: function(a) {
        if (!a && typeof(a) == "undefined") {
            return
        }
        if (typeof(a) == "string") {
            this.disableTab(this.links.find(function(b) {
                return b.key == a
            }))
        } else {
            if (typeof(a) == "number") {
                this.disableTab(this.links[a])
            } else {
                if ({
                    INPUT: true,
                    BUTTON: true,
                    SELECT: true,
                    TEXTAREA: true
                }[a.nodeName]) {
                    a.disabled = true
                }(this.options.setClassOnContainer ? $(a.parentNode) : a).addClassName(this.options.disabledClassName)
            }
        }
    },
    enableTab: function(a) {
        if (!a && typeof(a) == "undefined") {
            return
        }
        if (typeof(a) == "string") {
            this.enableTab(this.links.find(function(b) {
                return b.key == a
            }))
        } else {
            if (typeof(a) == "number") {
                this.enableTab(this.links[a])
            } else {
                if ({
                    INPUT: true,
                    BUTTON: true,
                    SELECT: true,
                    TEXTAREA: true
                }[a.nodeName]) {
                    a.disabled = false
                }(this.options.setClassOnContainer ? $(a.parentNode) : a).removeClassName(this.options.disabledClassName)
            }
        }
    },
    next: function() {
        this.links.each(function(b, a) {
            if (this.activeLink == b && this.links[a + 1]) {
                this.setActiveTab(this.links[a + 1]);
                throw $break
            }
        }.bind(this))
    },
    previous: function() {
        this.links.each(function(b, a) {
            if (this.activeLink == b && this.links[a - 1]) {
                this.setActiveTab(this.links[a - 1]);
                throw $break
            }
        }.bind(this))
    },
    first: function() {
        this.setActiveTab(this.links.first())
    },
    last: function() {
        this.setActiveTab(this.links.last())
    }
});
Object.extend(Control.Tabs, {
    instances: [],
    findByTabId: function(a) {
        return Control.Tabs.instances.find(function(b) {
            return b.links.find(function(c) {
                return c.key == a
            })
        })
    }
});
var _ga = _ga || {};
var _gaq = _gaq || [];
_ga.trackSocial = function(a, b) {
    _ga.trackFacebook(a, b);
    _ga.trackTwitter(a, b)
};
_ga.trackFacebook = function(a, b) {
    var d = _ga.buildTrackerName_(b);
    try {
        if (FB && FB.Event && FB.Event.subscribe) {
            FB.Event.subscribe("edge.create", function(e) {
                _gaq.push([d + "_trackSocial", "facebook", "like", e, a])
            });
            FB.Event.subscribe("edge.remove", function(e) {
                _gaq.push([d + "_trackSocial", "facebook", "unlike", e, a])
            });
            FB.Event.subscribe("message.send", function(e) {
                _gaq.push([d + "_trackSocial", "facebook", "send", e, a])
            })
        }
    } catch (c) {}
};
_ga.buildTrackerName_ = function(a) {
    return a ? a + "." : ""
};
_ga.trackTwitter = function(a, b) {
    var d = _ga.buildTrackerName_(b);
    try {
        if (twttr && twttr.events && twttr.events.bind) {
            twttr.events.bind("tweet", function(e) {
                if (e) {
                    var f;
                    if (e.target && e.target.nodeName == "IFRAME") {
                        f = _ga.extractParamFromUri_(e.target.src, "url")
                    }
                    _gaq.push([d + "_trackSocial", "twitter", "tweet", f, a])
                }
            })
        }
    } catch (c) {}
};
_ga.extractParamFromUri_ = function(b, e) {
    if (!b) {
        return
    }
    var d = b.split("#");
    if (d.length == 1) {
        return
    }
    var c = decodeURI(d[1]);
    e += "=";
    var g = c.split("&");
    for (var a = 0, f; f = g[a]; ++a) {
        if (f.indexOf(e) === 0) {
            return unescape(f.split("=")[1])
        }
    }
    return
};
LightboxOptions = Object.extend({
    fileLoadingImage: "/images/lb_loading.gif",
    fileBottomNavCloseImage: "/images/lb_closelabel.gif",
    overlayOpacity: 0.8,
    animate: true,
    resizeSpeed: 9,
    borderSize: 10,
    labelImage: "Image",
    labelOf: "of",
    imageLoadErrorHTML: '<div id="notfounderror">Image not found</div>'
}, window.LightboxOptions || {});
var Lightbox = Class.create();
Lightbox.prototype = {
    imageArray: [],
    activeImage: undefined,
    currentSet: undefined,
    changeImageHandlers: [],
    closeHandlers: [],
    initialize: function() {
        this.updateImageList();
        this.keyboardAction = this.keyboardAction.bindAsEventListener(this);
        if (LightboxOptions.resizeSpeed > 10) {
            LightboxOptions.resizeSpeed = 10
        }
        if (LightboxOptions.resizeSpeed < 1) {
            LightboxOptions.resizeSpeed = 1
        }
        this.resizeDuration = LightboxOptions.animate ? ((11 - LightboxOptions.resizeSpeed) * 0.15) : 0;
        this.overlayDuration = LightboxOptions.animate ? 0.2 : 0;
        var b = (LightboxOptions.animate ? 250 : 1) + "px";
        var a = $$("body")[0];
        a.appendChild(Builder.node("div", {
            id: "overlay"
        }));
        a.appendChild(Builder.node("div", {
            id: "lightbox"
        }, [Builder.node("div", {
            id: "outerImageContainer"
        }, Builder.node("div", {
            id: "imageContainer"
        }, [Builder.node("div", {
            id: "topNav"
        }, Builder.node("a", {
            id: "topNavClose",
            href: "#"
        }, Builder.node("img", {
            src: LightboxOptions.fileBottomNavCloseImage
        }))), Builder.node("img", {
            id: "lightboxImage"
        }), Builder.node("div", {
            id: "lightboxText"
        }), Builder.node("div", {
            id: "hoverNav"
        }, [Builder.node("a", {
            id: "prevLink",
            href: "#"
        }), Builder.node("a", {
            id: "nextLink",
            href: "#"
        })]), Builder.node("div", {
            id: "loading"
        }, Builder.node("a", {
            id: "loadingLink",
            href: "#"
        }, Builder.node("img", {
            src: LightboxOptions.fileLoadingImage
        })))])), Builder.node("div", {
            id: "imageDataContainer"
        }, Builder.node("div", {
            id: "imageData"
        }, [Builder.node("div", {
            id: "imageDetails"
        }, [Builder.node("span", {
            id: "caption"
        }), Builder.node("span", {
            id: "numberDisplay"
        })]), Builder.node("div", {
            id: "bottomNav"
        }, Builder.node("a", {
            id: "bottomNavClose",
            href: "#"
        }, Builder.node("img", {
            src: LightboxOptions.fileBottomNavCloseImage
        })))]))]));
        $("overlay").hide().observe("click", (function() {
            this.end()
        }).bind(this));
        $("lightbox").hide().observe("click", (function(d) {
            if (d.element().id == "lightbox") {
                this.end()
            }
        }).bind(this));
        $("outerImageContainer").setStyle({
            width: b,
            height: b
        });
        $("prevLink").observe("click", (function(d) {
            d.stop();
            this.changeImage(this.activeImage - 1)
        }).bindAsEventListener(this));
        $("nextLink").observe("click", (function(d) {
            d.stop();
            this.changeImage(this.activeImage + 1)
        }).bindAsEventListener(this));
        $("loadingLink").observe("click", (function(d) {
            d.stop();
            this.end()
        }).bind(this));
        $("bottomNavClose").observe("click", (function(d) {
            d.stop();
            this.end()
        }).bind(this));
        $("topNavClose").observe("click", (function(d) {
            d.stop();
            this.end()
        }).bind(this));
        var c = this;
        (function() {
            var d = "overlay lightbox outerImageContainer imageContainer lightboxImage lightboxText hoverNav prevLink nextLink loading loadingLink imageDataContainer imageData imageDetails caption numberDisplay bottomNav bottomNavClose topNav topNavClose";
            $w(d).each(function(e) {
                c[e] = $(e)
            })
        }).defer()
    },
    updateImageList: function() {
        this.updateImageList = Prototype.emptyFunction;
        document.observe("click", (function(a) {
            var b = a.findElement("a[rel^=lightbox]") || a.findElement("area[rel^=lightbox]");
            if (b) {
                a.stop();
                this.start(b)
            }
        }).bind(this))
    },
    start: function(c) {
        $$("select", "object", "embed").each(function(j) {
            j.style.visibility = "hidden"
        });
        new Effect.Appear(this.overlay, {
            duration: this.overlayDuration,
            from: 0,
            to: LightboxOptions.overlayOpacity
        });
        this.imageArray = [];
        var b = 0;
        var i = c.rel;
        this.currentSet = i;
        var g = undefined;
        var f = i.indexOf("#");
        if (f > 0) {
            g = i.substring(f);
            i = i.substring(0, f)
        }
        if (i == "lightbox") {
            var a = c.href;
            if (g) {
                a = g
            }
            this.imageArray.push([a, c.title])
        } else {
            this.imageArray = $$(c.tagName + '[href][rel="' + c.rel + '"]').collect(function(j) {
                if (j.hasClassName("lightboxignore") || j.up(".lightboxignore")) {
                    return null
                } else {
                    return [j.href, j.title]
                }
            }).compact().uniq();
            while (b < this.imageArray.length && this.imageArray[b][0] != c.href) {
                b++
            }
        }
        var d = document.viewport.getScrollOffsets();
        var e = d[1] + (document.viewport.getHeight() / 10);
        var h = d[0];
        this.lightbox.setStyle({
            top: e + "px",
            left: h + "px"
        }).show();
        this.changeImage(b)
    },
    changeImage: function(d) {
        this.activeImage = d;
        if (this.changeImageHandlers.length > 0) {
            var e = this.imageArray[d][0];
            var f = this.currentSet;
            this.changeImageHandlers.each(function(k) {
                k.apply(this, [e, f])
            })
        }
        if (LightboxOptions.animate) {
            this.loading.show()
        }
        this.lightboxImage.hide();
        this.hoverNav.hide();
        this.prevLink.hide();
        this.nextLink.hide();
        this.imageDataContainer.setStyle({
            opacity: 0.0001
        });
        this.numberDisplay.hide();
        var b = this.imageArray[this.activeImage][0];
        if (!b.startsWith("#")) {
            var g = new Image();
            this.lightboxText.innerHTML = "";
            g.onerror = (function() {
                this.lightboxImage.hide();
                this.lightboxText.innerHTML = LightboxOptions.imageLoadErrorHTML;
                this.resizeImageContainer(200, 200, true)
            }).bind(this);
            g.onload = (function() {
                this.lightboxImage.src = this.imageArray[this.activeImage][0];
                this.lightboxImage.width = g.width;
                this.lightboxImage.height = g.height;
                this.resizeImageContainer(g.width, g.height, false)
            }).bind(this);
            g.src = this.imageArray[this.activeImage][0]
        } else {
            var i = b.substring(1);
            var c = false;
            if (i.indexOf("#") > 0) {
                var h = i.split("#");
                i = h[0];
                c = parseInt(h[1])
            }
            var a = $(i);
            if (!c) {
                c = a.readAttribute("data-width")
            }
            if (!c || c == "") {
                c = 800
            }
            this.lightbox.classNames = "";
            if (a.readAttribute("data-close-on-top") == "1") {
                this.lightbox.addClassName("closeOnTop")
            }
            var j = a.readAttribute("data-css");
            if (j && j != "") {
                this.lightbox.addClassName(j)
            }
            this.lightboxImage.hide();
            this.lightboxText.innerHTML = a.innerHTML;
            this.resizeImageContainer(c, 800, true)
        }
    },
    resizeImageContainer: function(f, g, c) {
        var i = this.outerImageContainer.getWidth();
        var d = this.outerImageContainer.getHeight();
        var h = (f + LightboxOptions.borderSize * 2);
        var k = (g + LightboxOptions.borderSize * 2);
        var l = (h / i) * 100;
        var b = (k / d) * 100;
        var j = i - h;
        var a = d - k;
        if (a != 0 && !c) {
            new Effect.Scale(this.outerImageContainer, b, {
                scaleX: false,
                duration: this.resizeDuration,
                queue: "front"
            })
        }
        if (j != 0 && !c) {
            new Effect.Scale(this.outerImageContainer, l, {
                scaleY: false,
                duration: this.resizeDuration,
                delay: this.resizeDuration
            })
        }
        if (c) {
            this.outerImageContainer.setStyle({
                width: h + "px"
            });
            this.outerImageContainer.setStyle({
                height: "auto"
            })
        }
        var e = 0;
        if ((a == 0) && (j == 0)) {
            e = 100;
            if (Prototype.Browser.IE) {
                e = 250
            }
        }(function() {
            this.prevLink.setStyle({
                height: g + "px"
            });
            this.nextLink.setStyle({
                height: g + "px"
            });
            this.imageDataContainer.setStyle({
                width: h + "px"
            });
            this.showImage(c);
            scrollElementInViewport(this.topNavClose, 20, 20)
        }).bind(this).delay(e / 1000)
    },
    showImage: function(a) {
        this.loading.hide();
        if (!a) {
            new Effect.Appear(this.lightboxImage, {
                duration: this.resizeDuration,
                queue: "end",
                afterFinish: (function() {
                    this.updateDetails(false)
                }).bind(this)
            });
            this.preloadNeighborImages()
        } else {
            this.updateDetails(true)
        }
    },
    updateDetails: function(a) {
        if (a) {
            $$("#lightbox select", "#lightbox object", "#lightbox embed").each(function(b) {
                b.style.visibility = "visible"
            })
        }
        this.caption.update(this.imageArray[this.activeImage][1]).show();
        if (this.imageArray.length > 1) {
            this.numberDisplay.update(LightboxOptions.labelImage + " " + (this.activeImage + 1) + " " + LightboxOptions.labelOf + "  " + this.imageArray.length).show()
        }
        new Effect.Parallel([new Effect.SlideDown(this.imageDataContainer, {
            sync: true,
            duration: this.resizeDuration,
            from: 0,
            to: 1
        }), new Effect.Appear(this.imageDataContainer, {
            sync: true,
            duration: this.resizeDuration
        })], {
            duration: this.resizeDuration,
            afterFinish: (function() {
                if (!a) {
                    this.updateNav()
                }
            }).bind(this)
        })
    },
    updateNav: function() {
        this.hoverNav.show();
        if (this.activeImage > 0) {
            this.prevLink.show()
        }
        if (this.activeImage < (this.imageArray.length - 1)) {
            this.nextLink.show()
        }
        this.enableKeyboardNav()
    },
    enableKeyboardNav: function() {
        document.observe("keydown", this.keyboardAction)
    },
    disableKeyboardNav: function() {
        document.stopObserving("keydown", this.keyboardAction)
    },
    keyboardAction: function(d) {
        var a = d.keyCode;
        var b;
        if (d.DOM_VK_ESCAPE) {
            b = d.DOM_VK_ESCAPE
        } else {
            b = 27
        }
        var c = String.fromCharCode(a).toLowerCase();
        if (c.match(/x|o|c/) || (a == b)) {
            this.end()
        } else {
            if ((c == "p") || (a == 37)) {
                if (this.activeImage != 0) {
                    this.disableKeyboardNav();
                    this.changeImage(this.activeImage - 1)
                }
            } else {
                if ((c == "n") || (a == 39)) {
                    if (this.activeImage != (this.imageArray.length - 1)) {
                        this.disableKeyboardNav();
                        this.changeImage(this.activeImage + 1)
                    }
                }
            }
        }
    },
    preloadNeighborImages: function() {
        var a, b;
        if (this.imageArray.length > this.activeImage + 1) {
            a = new Image();
            a.src = this.imageArray[this.activeImage + 1][0]
        }
        if (this.activeImage > 0) {
            b = new Image();
            b.src = this.imageArray[this.activeImage - 1][0]
        }
    },
    end: function() {
        if (this.closeHandlers.length > 0) {
            this.closeHandlers.each(function(a) {
                a.call(this)
            })
        }
        this.disableKeyboardNav();
        this.lightbox.hide();
        new Effect.Fade(this.overlay, {
            duration: this.overlayDuration
        });
        $$("select", "object", "embed").each(function(a) {
            a.style.visibility = "visible"
        })
    },
    getPageSize: function() {
        var c, a;
        if (window.innerHeight && window.scrollMaxY) {
            c = window.innerWidth + window.scrollMaxX;
            a = window.innerHeight + window.scrollMaxY
        } else {
            if (document.body.scrollHeight > document.body.offsetHeight) {
                c = document.body.scrollWidth;
                a = document.body.scrollHeight
            } else {
                c = document.body.offsetWidth;
                a = document.body.offsetHeight
            }
        }
        var b, d;
        if (self.innerHeight) {
            if (document.documentElement.clientWidth) {
                b = document.documentElement.clientWidth
            } else {
                b = self.innerWidth
            }
            d = self.innerHeight
        } else {
            if (document.documentElement && document.documentElement.clientHeight) {
                b = document.documentElement.clientWidth;
                d = document.documentElement.clientHeight
            } else {
                if (document.body) {
                    b = document.body.clientWidth;
                    d = document.body.clientHeight
                }
            }
        } if (a < d) {
            pageHeight = d
        } else {
            pageHeight = a
        } if (c < b) {
            pageWidth = c
        } else {
            pageWidth = b
        }
        return [pageWidth, pageHeight]
    }
};
var LightboxInstance = undefined;

