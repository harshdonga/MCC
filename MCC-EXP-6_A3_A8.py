table0=[197, 235, 60, 151, 98, 96, 3, 100, 248, 118, 42, 117, 172, 211, 181, 203, 61,
		126, 156, 87, 149, 224, 55, 132, 186, 63, 238, 255, 85, 83, 152, 33, 160,
		184, 210, 219, 159, 11, 180, 194, 130, 212, 147, 5, 215, 92, 27, 46, 113,
		187, 52, 25, 185, 79, 221, 48, 70, 31, 101, 15, 195, 201, 50, 222, 137,
		233, 229, 106, 122, 183, 178, 177, 144, 207, 234, 182, 37, 254, 227, 231, 54,
		209, 133, 65, 202, 69, 237, 220, 189, 146, 120, 68, 21, 125, 38, 30, 2,
		155, 53, 196, 174, 176, 51, 246, 167, 76, 110, 20, 82, 121, 103, 112, 56,
		173, 49, 217, 252, 0, 114, 228, 123, 12, 93, 161, 253, 232, 240, 175, 67,
		128, 22, 158, 89, 18, 77, 109, 190, 17, 62, 4, 153, 163, 59, 145, 138,
		7, 74, 205, 10, 162, 80, 45, 104, 111, 150, 214, 154, 28, 191, 169, 213,
		88, 193, 198, 200, 245, 39, 164, 124, 84, 78, 1, 188, 170, 23, 86, 226,
		141, 32, 6, 131, 127, 199, 40, 135, 16, 57, 71, 91, 225, 168, 242, 206,
		97, 166, 44, 14, 90, 236, 239, 230, 244, 223, 108, 102, 119, 148, 251, 29,
		216, 8, 9, 249, 208, 24, 105, 94, 34, 64, 95, 115, 72, 134, 204, 43,
		247, 243, 218, 47, 58, 73, 107, 241, 179, 116, 66, 36, 143, 81, 250, 139,
		19, 13, 142, 140, 129, 192, 99, 171, 157, 136, 41, 75, 35, 165, 26 ]

table1=[170, 42, 95, 141, 109, 30, 71, 89, 26, 147, 231, 205, 239, 212, 124, 129, 216,
		79, 15, 185, 153, 14, 251, 162, 0, 241, 172, 197, 43, 10, 194, 235, 6,
		20, 72, 45, 143, 104, 161, 119, 41, 136, 38, 189, 135, 25, 93, 18, 224,
		171, 252, 195, 63, 19, 58, 165, 23, 55, 133, 254, 214, 144, 220, 178, 156,
		52, 110, 225, 97, 183, 140, 39, 53, 88, 219, 167, 16, 198, 62, 222, 76,
		139, 175, 94, 51, 134, 115, 22, 67, 1, 249, 217, 3, 5, 232, 138, 31,
		56, 116, 163, 70, 128, 234, 132, 229, 184, 244, 13, 34, 73, 233, 154, 179,
		131, 215, 236, 142, 223, 27, 57, 246, 108, 211, 8, 253, 85, 66, 245, 193,
		78, 190, 4, 17, 7, 150, 127, 152, 213, 37, 186, 2, 243, 46, 169, 68,
		101, 60, 174, 208, 158, 176, 69, 238, 191, 90, 83, 166, 125, 77, 59, 21,
		92, 49, 151, 168, 99, 9, 50, 146, 113, 117, 228, 65, 230, 40, 82, 54,
		237, 227, 102, 28, 36, 107, 24, 44, 126, 206, 201, 61, 114, 164, 207, 181,
		29, 91, 64, 221, 255, 48, 155, 192, 111, 180, 210, 182, 247, 203, 148, 209,
		98, 173, 11, 75, 123, 250, 118, 32, 47, 240, 202, 74, 177, 100, 80, 196,
		33, 248, 86, 157, 137, 120, 130, 84, 204, 122, 81, 242, 188, 200, 149, 226,
		218, 160, 187, 106, 35, 87, 105, 96, 145, 199, 159, 12, 121, 103, 112]


def helper(KXOR,RAND):
	temp = [0] * 16
	KM_RM = RAND + KXOR

	for i in range(5):
		for z in range(16):
			temp[z] = table0[table1[KM_RM[16+z]] ^ KM_RM[z] ]

		j = 0
		while ( (1 << i) > j):
			k = 0
			while ( (1 << (4 - i)) > k ):
				KM_RM[((2 * k + 1) << i )+j] = table0[table1[temp[(k << i) + j]] ^ (KM_RM[(k << i) + 16 + j])]
				KM_RM[ (k << (i + 1)) + j] = temp[(k << i) + j]
				k = k+1
			j = j + 1
		
	output = [0]*16

	for i in range(16):
		for j in range(8):
			output[i] = output[i] ^ (((KM_RM[(19 * (j + 8 * i) + 19) % 256 / 8] >> (3 * j + 3) % 8) & 1) << j)

	return output
	
def compute(K, RAND, version = 2):
	
	K_MIX = [0]*16
	RAND_MIX = [0]*16
	KATYVASZ = [0]*16
	output = [0]*16
	
	for i in range(8):
		K_MIX[i] = K[15 - i]
		K_MIX[15 - i] = K[i]

	for i in range(8):
		RAND_MIX[i] = RAND[15 - i]
		RAND_MIX[15 - i] = RAND[i]
	
	for i in range(16):
		KATYVASZ[i] = K_MIX[i] ^ RAND_MIX[i]
	
	for i in range(8):
		RAND_MIX = helper(KATYVASZ,RAND_MIX)
	
	for i in range(16):
		output[i] = RAND_MIX[15-i]
	

	if version == 2:
		output[15] = 0
		output[14] = 4 * (output[14] >> 2)

	s = 8
	i = 0
	while i < 4:
		output[s+i-4] = output[s+i]
		output[s+i] = output[s+i+4]
		i = i+1
	
	output_final = output[:12]	
	return output_final
	
	
def hex2intarr(input):
	return map(lambda a: int(a.encode('hex'),16), (a for a in input.decode('hex')))
		
def intarr2hex(input):
	return ''.join('{:02x}'.format(x) for x in input).upper()

if __name__ == '__main__':
	import argparse
	
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('Ki', metavar='Ki', default = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" ,nargs='?', help='The super secret Ki key')
	parser.add_argument('RAND', metavar='RAND', default = "6E6989BE6CEE7154543770AE80B1EF0D", nargs='?', help='The RANDom number you recieve from the tower')
	parser.add_argument('version', metavar='version', default = 2, nargs='?', help='The version of the COMP128 algo you wish to use (options: 2 or 3)')

	args = parser.parse_args()

	Ki = hex2intarr(args.Ki)
	RAND = hex2intarr(args.RAND)
	version = args.version

	print 'INPUTS:\n\nKi:      ' + intarr2hex(Ki)
	print 'RAND:    ' + intarr2hex(RAND)

	OUTPUT = compute(Ki, RAND, version)
	SRES = OUTPUT[:4]
	Kc = OUTPUT[4:]
	
	print "\n\nOUTPUT:\n\nSIM OUTPUT: " + intarr2hex(OUTPUT)
	print "A3 output SRES:  " + intarr2hex(SRES)
	print "A8 output Kc  :  " + intarr2hex(Kc)
