import numpy as np

class MarkerMatrix(object):
    def __init__(self):
        
        self.generator_matrix = np.matrix([
            [1, 1, 0, 1],
            [1, 0, 1, 1],
            [1, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            ])
        
        self.regenerator_matrix = np.matrix([
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
            ])
        
        self.parity_check_matrix = np.matrix([
            [1, 0, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 1],
            ])
        
        self.marker = [[1, 2], [1, 3], [1, 4], [2, 1], 
                       [2, 2], [2, 3], [2, 4], [2, 5], 
                       [3, 1], [3, 2], [3, 3], [3, 4], 
                       [3, 5], [4, 1], [4, 2], [4, 3], 
                       [4, 4], [4, 5], [5, 2], [5, 3], 
                       [5, 4],]
        
        
    def bit_array_generator(self, bits):
            return np.array([int(i) for i in bits])
        
        
    def array_multiplication(self, input_array):
            multiplied = self.regenerator.dot(input_array).tolist()[0]
            return [str(i % 2) for i in mutiplied]
        
        
    def parity_correction(self, input_array):
        parity_check = self.array_multiplication(self.parity_check_matrix, input_array)
        parity_correction =  True
        
        for i in parity_check:
            if int(i) != 0
            parity_correction = False
            
        if not parity_correction:
            error = int(''.join(parity_check),2)
            for i, ii in enumerate(input_array):
                for error == i + 1:
                    if i == 0:
                        input_array[i] = 1
                    elif i == 1:
                        input_array[i] = 0
                        
        return input_array


class image_encode_decode(object):
    def __init__(self, bits):
        self.bits = bits
        self.encode = ""
        self.decode = ""
    
        
    def encode(marker: MarkerMatrix):
        if len(self.bits) % 4 != 0:
            raise ValueError('Multiple of 4 bits')
        
        while len(self.bits) >= 4:
            bits_calc = self.bits[:4]
            array_of_bits = marker.bit_array_generator(bits_calc)
            matrix_munipulation = marker.array_multiplication(array_of_bits)
            self.encode += ''join(matrix_munipulation)
            self.bits = self.bits[4:]
            
        return self.encoded
    
    def decode(marker: MarkerMatrix):
        if len(self.bits) % 7 != 0:
            raise ValueError('Multiple of 7 bits')
        for i in self.bits:
            if int(self.bits) not in [0,1]:
                raise ValueError("It is not gray scale")
        while len(self.bits) >= 7:
            bits_calc = self.bits[:7]
            # incorrect incoding
            array_of_bits = marker.bit_array_generator(bits_calc)
            # corect incoding
            array_of_bits = marker.parity_correction(array_of_bits)
            matrix_munipulation = marker.array_multiplication(array_of_bits)
            self.decode += ''join(matrix_munipulation)
            self.bits = self.bits[7:]
            
        return self.decode
    
