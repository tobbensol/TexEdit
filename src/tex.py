# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum, IntFlag

if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))


class Tex(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.hdr = Tex.Header(self._io, self, self._root)
        self.bdy = Tex.Body(self._io, self, self._root)

    def _write(self, file):
        with open(file, "wb") as f:
            f.write(self.hdr.data + b''.join(self.bdy.data))

    class Header(KaitaiStruct):

        class Attribute(IntFlag):
            discard_per_frame = 1
            discard_per_map = 2
            managed = 4
            user_managed = 8
            cpu_read = 16
            location_main = 32
            no_gpu_read = 64
            aligned_size = 128
            edge_culling = 256
            location_onion = 512
            read_write = 1024
            immutable = 2048
            texture_render_target = 1048576
            texture_depth_stencil = 2097152
            texture_type_1d = 4194304
            texture_type_2d = 8388608
            texture_type_3d = 16777216
            texture_type_cube = 33554432
            texture_type_mask = 62914560
            texture_swizzle = 67108864
            texture_no_tiled = 134217728
            texture_no_swizzle = 2147483648

        class TextureFormat(IntFlag):
            enum_shift = 0
            type_integer = 1
            type_float = 2
            type_dxt = 3
            bpp_shift = 4
            type_special = 5
            type_bc57 = 6
            component_shift = 8
            type_shift = 12
            enum_mask = 15
            bpp_mask = 240
            component_mask = 3840
            l8 = 4400
            a8 = 4401
            b4g4r4a4 = 5184
            b5g5r5a1 = 5185
            b8g8r8a8 = 5200
            b8g8r8x8 = 5201
            r32f = 8528
            r16g16f = 8784
            r32g32f = 8800
            r16g16b16a16f = 9312
            r32g32b32a32f = 9328
            dxt1 = 13344
            dxt3 = 13360
            dxt5 = 13361
            d16 = 16704
            d24s8 = 16976
            null1 = 20736
            shadow16 = 20800
            shadow24 = 20816
            ati2 = 25136
            bc7 = 25650
            type_mask = 61440

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = []

            self.data.append(self._io.read_bytes(4))
            self.type = KaitaiStream.resolve_enum(Tex.Header.Attribute, KaitaiStream.packer_u4le.unpack(self.data[-1])[0])
            self.data.append(self._io.read_bytes(4))
            self.format = KaitaiStream.resolve_enum(Tex.Header.TextureFormat, KaitaiStream.packer_u4le.unpack(self.data[-1])[0])

            self.data.append(self._io.read_bytes(2))
            self.width = KaitaiStream.packer_u2le.unpack(self.data[-1])[0]
            self.data.append(self._io.read_bytes(2))
            self.height = KaitaiStream.packer_u2le.unpack(self.data[-1])[0]
            self.data.append(self._io.read_bytes(2))
            self.depth = KaitaiStream.packer_u2le.unpack(self.data[-1])[0]
            self.data.append(self._io.read_bytes(2))
            self.mip_levels = KaitaiStream.packer_u2le.unpack(self.data[-1])[0]

            self.lod_offset3 = []
            for i in range(3):
                self.data.append(self._io.read_bytes(4))
                self.lod_offset3.append(KaitaiStream.packer_u4le.unpack(self.data[-1])[0])

            self.offset_to_surface13 = []
            for i in range(13):
                self.data.append(self._io.read_bytes(4))
                self.offset_to_surface13.append(KaitaiStream.packer_u4le.unpack(self.data[-1])[0])
            self.data = b''.join(self.data)
            

    class Body(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = []
            i = 0
            while not self._io.is_eof():
                self.data.append(self._io.read_bytes(1))
                i += 1
                
    