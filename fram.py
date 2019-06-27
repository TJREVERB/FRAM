import time
import spidev

WREN = 0x06
WRITE = 0x02
READ = 0x03
SLEEP = 0xA9
spi = spidev.SpiDev()

def start():
    global spi

    bus = 0 #Only have SPI Bus 0 available on RPI
    device = 1 #Device is the chip select pin. Set to 0 or 1, depending on connection
    spi.open(bus, device) #Opens connection with specific bus and device
    spi.max_speed_hz = 31200000 #FRAM max is 40MHz and RPI only supports certain numbers
    spi.mode=0
    spi.cshigh = True

def write_to_fram(address, to_send):
    spi.xfer([WREN])
    spi.xfer([WRITE, address, to_send])

def read_from_fram(address, num_bytes):
    spi.xfer([READ, address])
    return spi.readBytes(num_bytes)
        
if __name__ == "__main__":
    start()