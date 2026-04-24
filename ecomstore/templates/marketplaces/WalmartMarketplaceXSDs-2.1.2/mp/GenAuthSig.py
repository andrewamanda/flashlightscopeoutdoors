from subprocess import *

def jarWrapper(*args):
    process = Popen(['java', '-jar']+list(args), stdout=PIPE, stderr=PIPE)
    ret = []
    while process.poll() is None:
        line = process.stdout.readline()
        if line != '' and line.endswith('\n'):
            ret.append(line[:-1])
    stdout, stderr = process.communicate()
    ret += stdout.split('\n')
    if stderr != '':
        ret += stderr.split('\n')
    ret.remove('')
    return ret

args = ['DigitalSignatureUtil-1.0.0.jar', 'DigitalSignatureUtil', 'https://marketplace.walmartapis.com/v2/feeds/d4885da4-9bc1-4296-b26f-57e3cb0e0fc9?includeDetails=true', '04aaea70-b106-4b25-9f8f-d9f693767084', 'MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAK4avzZ/W8vqTkHNS9OWVy9mBHc3KG3DSr42AFyLGJNCfxl2BDOt9oyVN3oO03FvIfdUgubJOwTcgG3l15sPyX/Uk6vJVoHnaqO38a+q+H8cWkVCjigK7xoeusDGTxOr1Rcz2IQhTeIipus5xddR+dIacEBl9w/ou/GeCpdyarSvAgMBAAECgYBByEVbF//dKihrYGA4D+PdOtSRHrwdzN4exFSaosukSEmxmw+3XxF6yJ5vdc6aW30f8ESNYpb0HURBQciXA/4DuMu3066vj4Rqes34ThHjisHzKIpmL3/iVLak4NipdiKl2zDO3EkBhS2QAOMfKfzC1rOM/Ip/wIfuK6CvjZ9CUQJBAN8sGEQRXkMgky56tHON4T8EFlxDaDHE/I2lsKuMJrWDnUzs3uHzDENSu0ZRQRd6YgVkq0p3wYPv8wEDiCY6tEMCQQDHtu1zS+3WqImBKzBwMW2zmGl41Va6cCEIxTvcrHJcZhIF8xawpQalq63zdubwfwQH1Car45X8q+rkanY5R80lAkEAz2KlhhNxugV6YDXMnJka2LlOohxNpfo9CtAO9cs+aWzN7x8rG2MFYUZvGzAEwfGLRyG+f2v720ROWAHVMllZCwJAG6xMQLKftSPLUdujLZibw8v1qWmeR90rpqR1xAEdI5J9ItfpJ/bl8eTVCKxMGbzv2QnbhevWJ5nGxXm/AfbiBQJBAKhWRK8Crl4p95kfKYbdSG7UU29VWxy1wDVufSKc3Szh50KuVmFTNqwpjPQgtEOMEpoQMzXiniJoYlLuh2CcIgw=', 'POST', 'Hello'] # Any number of args to be passed to the jar file

result = jarWrapper(*args)

print result
