
def set_bit(bit):
		reg = (1<<bit)
		
		return reg
		
		
def clear_bit(bit):
		reg &= ~(1<<bit)
		return reg
		
def toggle_bit(bit):
		reg ^= (1<<bit)
		return reg
		
def get_bit(reg,bit):
		return((reg>>bit) & 0x01)
		
print(set_bit(0))
print(clear_bit(0))
print(toggle_bit(0))
print(get_bit(1,0))