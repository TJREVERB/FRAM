import time
import spidev

WREN = 0x06
WRITE = 0x02
spi = spidev.SpiDev()

#Only have SPI Bus 0 available on RPI
bus = 0

#Device is the chip select pin. Set to 0 or 1, depending on connection
device = 1

#Opens connection with specific bus and device
spi.open(bus, device)

spi.max_speed_hz = 31200000
spi.mode=0

spi.xfer([WREN])
spi.xfer([WRITE, 0x01, 0x06])