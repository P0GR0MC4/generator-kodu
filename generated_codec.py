import struct

class TelemetryData:
    def __init__(self, device_id, temperature, status_code):
        
        self.device_id = device_id
        
        self.temperature = temperature
        
        self.status_code = status_code
        

    def serialize(self) -> bytes:
        # Format: ifi
        return struct.pack('ifi', self.device_id, self.temperature, self.status_code)

    @classmethod
    def deserialize(cls, data: bytes):
        unpacked = struct.unpack('ifi', data)
        return cls(unpacked[0], unpacked[1], unpacked[2])

    def __repr__(self):
        return f"TelemetryData(device_id={self.device_id}, temperature={self.temperature}, status_code={self.status_code})"