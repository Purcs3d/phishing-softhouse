""" Web configurations """
HOST = '127.0.0.0' # aka localhost
PORT = '8000' # aka localhost:8000

""" SSL/TSL """

BAD_CERT_VERSIONS = ["SSL1.0", "SSL2.0", "SSL3.0", "TLSv1.0", "TLSv1.1", "TLSv1.2"]
# list of whitelisted SSL/TSL license versions
MIN_CERT_VER = 2 #? TLSv1.2 is permitted some bigger sites still use it
# whitelisted "safe" hashing algorithms used on the cert
WHITE_CRT_HASH = []
# minimum age a license should be without being triggered as phishy (in days)
MIN_CRT_AGE = 30
