""" Web configurations """
HOST = '127.0.0.0' # aka localhost 
PORT = '8000' # aka localhost:8000

""" SSL/TSL """

# list of whitelisted SSL/TSL license versions
WHITE_CRT_VER = ['TLSv1.3', 'TLSv1.2'] #? TLSv1.2 is permitted somew bigger sites still use it
# whitelisted "safe" hashing algorithms used on the cert
WHITE_CRT_HASH = []
# minimum age a license should be without being triggered as phishy (in days)
MIN_CRT_AGE = 30
