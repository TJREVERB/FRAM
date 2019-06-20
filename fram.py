import time
import spidev

spi = spidev.SpiDev()

#Only have SPI Bus 0 available on RPI
bus = 0

#Device is the chip select pin. Set to 0 or 1, depending on connection
device = 1

#Opens connection with specific bus and device
spi.open(bus, device)

spi.max_speed_hz = 500000
spi.mode=0

writeByte = [0x02, 0x00]
spi.xfer(writeByte)