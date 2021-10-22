import numpy as np
from sys import platform
from fractions import Fraction
import logging

if platform == 'linux':
    from smbus2 import SMBus
from types import SimpleNamespace

SI5351_REGISTER_0_DEVICE_STATUS = 0
SI5351_REGISTER_1_INTERRUPT_STATUS_STICKY = 1
SI5351_REGISTER_2_INTERRUPT_STATUS_MASK = 2
SI5351_REGISTER_3_OUTPUT_ENABLE_CONTROL = 3
SI5351_REGISTER_9_OEB_PIN_ENABLE_CONTROL = 9
SI5351_REGISTER_15_PLL_INPUT_SOURCE = 15
SI5351_REGISTER_16_CLK0_CONTROL = 16
SI5351_REGISTER_17_CLK1_CONTROL = 17
SI5351_REGISTER_18_CLK2_CONTROL = 18
SI5351_REGISTER_19_CLK3_CONTROL = 19
SI5351_REGISTER_20_CLK4_CONTROL = 20
SI5351_REGISTER_21_CLK5_CONTROL = 21
SI5351_REGISTER_22_CLK6_CONTROL = 22
SI5351_REGISTER_23_CLK7_CONTROL = 23
SI5351_REGISTER_24_CLK3_0_DISABLE_STATE = 24
SI5351_REGISTER_25_CLK7_4_DISABLE_STATE = 25
SI5351_REGISTER_26_MULTISYNTH_NA_PARAMETERS_1 = 26
SI5351_REGISTER_26_MULTISYNTH_NA_PARAMETERS_2 = 27
SI5351_REGISTER_26_MULTISYNTH_NA_PARAMETERS_3 = 28
SI5351_REGISTER_26_MULTISYNTH_NA_PARAMETERS_4 = 29
SI5351_REGISTER_26_MULTISYNTH_NA_PARAMETERS_5 = 30
SI5351_REGISTER_26_MULTISYNTH_NA_PARAMETERS_6 = 31
SI5351_REGISTER_26_MULTISYNTH_NA_PARAMETERS_7 = 32
SI5351_REGISTER_26_MULTISYNTH_NA_PARAMETERS_8 = 33
SI5351_REGISTER_26_MULTISYNTH_NB_PARAMETERS_1 = 34
SI5351_REGISTER_26_MULTISYNTH_NB_PARAMETERS_2 = 35
SI5351_REGISTER_26_MULTISYNTH_NB_PARAMETERS_3 = 36
SI5351_REGISTER_26_MULTISYNTH_NB_PARAMETERS_4 = 37
SI5351_REGISTER_26_MULTISYNTH_NB_PARAMETERS_5 = 38
SI5351_REGISTER_26_MULTISYNTH_NB_PARAMETERS_6 = 39
SI5351_REGISTER_26_MULTISYNTH_NB_PARAMETERS_7 = 40
SI5351_REGISTER_26_MULTISYNTH_NB_PARAMETERS_8 = 41
SI5351_REGISTER_42_MULTISYNTH0_PARAMETERS_1 = 42
SI5351_REGISTER_43_MULTISYNTH0_PARAMETERS_2 = 43
SI5351_REGISTER_44_MULTISYNTH0_PARAMETERS_3 = 44
SI5351_REGISTER_45_MULTISYNTH0_PARAMETERS_4 = 45
SI5351_REGISTER_46_MULTISYNTH0_PARAMETERS_5 = 46
SI5351_REGISTER_47_MULTISYNTH0_PARAMETERS_6 = 47
SI5351_REGISTER_48_MULTISYNTH0_PARAMETERS_7 = 48
SI5351_REGISTER_49_MULTISYNTH0_PARAMETERS_8 = 49
SI5351_REGISTER_50_MULTISYNTH1_PARAMETERS_1 = 50
SI5351_REGISTER_51_MULTISYNTH1_PARAMETERS_2 = 51
SI5351_REGISTER_52_MULTISYNTH1_PARAMETERS_3 = 52
SI5351_REGISTER_53_MULTISYNTH1_PARAMETERS_4 = 53
SI5351_REGISTER_54_MULTISYNTH1_PARAMETERS_5 = 54
SI5351_REGISTER_55_MULTISYNTH1_PARAMETERS_6 = 55
SI5351_REGISTER_56_MULTISYNTH1_PARAMETERS_7 = 56
SI5351_REGISTER_57_MULTISYNTH1_PARAMETERS_8 = 57
SI5351_REGISTER_58_MULTISYNTH2_PARAMETERS_1 = 58
SI5351_REGISTER_59_MULTISYNTH2_PARAMETERS_2 = 59
SI5351_REGISTER_60_MULTISYNTH2_PARAMETERS_3 = 60
SI5351_REGISTER_61_MULTISYNTH2_PARAMETERS_4 = 61
SI5351_REGISTER_62_MULTISYNTH2_PARAMETERS_5 = 62
SI5351_REGISTER_63_MULTISYNTH2_PARAMETERS_6 = 63
SI5351_REGISTER_64_MULTISYNTH2_PARAMETERS_7 = 64
SI5351_REGISTER_65_MULTISYNTH2_PARAMETERS_8 = 65
SI5351_REGISTER_66_MULTISYNTH3_PARAMETERS_1 = 66
SI5351_REGISTER_67_MULTISYNTH3_PARAMETERS_2 = 67
SI5351_REGISTER_68_MULTISYNTH3_PARAMETERS_3 = 68
SI5351_REGISTER_69_MULTISYNTH3_PARAMETERS_4 = 69
SI5351_REGISTER_70_MULTISYNTH3_PARAMETERS_5 = 70
SI5351_REGISTER_71_MULTISYNTH3_PARAMETERS_6 = 71
SI5351_REGISTER_72_MULTISYNTH3_PARAMETERS_7 = 72
SI5351_REGISTER_73_MULTISYNTH3_PARAMETERS_8 = 73
SI5351_REGISTER_74_MULTISYNTH4_PARAMETERS_1 = 74
SI5351_REGISTER_75_MULTISYNTH4_PARAMETERS_2 = 75
SI5351_REGISTER_76_MULTISYNTH4_PARAMETERS_3 = 76
SI5351_REGISTER_77_MULTISYNTH4_PARAMETERS_4 = 77
SI5351_REGISTER_78_MULTISYNTH4_PARAMETERS_5 = 78
SI5351_REGISTER_79_MULTISYNTH4_PARAMETERS_6 = 79
SI5351_REGISTER_80_MULTISYNTH4_PARAMETERS_7 = 80
SI5351_REGISTER_81_MULTISYNTH4_PARAMETERS_8 = 81
SI5351_REGISTER_82_MULTISYNTH5_PARAMETERS_1 = 82
SI5351_REGISTER_83_MULTISYNTH5_PARAMETERS_2 = 83
SI5351_REGISTER_84_MULTISYNTH5_PARAMETERS_3 = 84
SI5351_REGISTER_85_MULTISYNTH5_PARAMETERS_4 = 85
SI5351_REGISTER_86_MULTISYNTH5_PARAMETERS_5 = 86
SI5351_REGISTER_87_MULTISYNTH5_PARAMETERS_6 = 87
SI5351_REGISTER_88_MULTISYNTH5_PARAMETERS_7 = 88
SI5351_REGISTER_89_MULTISYNTH5_PARAMETERS_8 = 89
SI5351_REGISTER_90_MULTISYNTH6_PARAMETERS = 90
SI5351_REGISTER_91_MULTISYNTH7_PARAMETERS = 91
SI5351_REGISTER_092_CLOCK_6_7_OUTPUT_DIVIDER = 92
SI5351_REGISTER_165_CLK0_INITIAL_PHASE_OFFSET = 165
SI5351_REGISTER_166_CLK1_INITIAL_PHASE_OFFSET = 166
SI5351_REGISTER_167_CLK2_INITIAL_PHASE_OFFSET = 167
SI5351_REGISTER_168_CLK3_INITIAL_PHASE_OFFSET = 168
SI5351_REGISTER_169_CLK4_INITIAL_PHASE_OFFSET = 169
SI5351_REGISTER_170_CLK5_INITIAL_PHASE_OFFSET = 170
SI5351_REGISTER_177_PLL_RESET = 177
SI5351_REGISTER_183_CRYSTAL_INTERNAL_LOAD_CAPACITANCE = 183

SI5351_I2C_ADDRESS_DEFAULT = 0x60

SI5351_CRYSTAL_LOAD_6PF = (1 << 6)
SI5351_CRYSTAL_LOAD_8PF = (2 << 6)
SI5351_CRYSTAL_LOAD_10PF = (3 << 6)

SI5351_CRYSTAL_FREQ_25MHZ = 25000000
SI5351_CRYSTAL_FREQ_27MHZ = 27000000

SI5351_VCO_MIN_FREQ = 600e6
SI5351_VCO_MAX_FREQ = 900e6

SI5351_PLL_A = 1
SI5351_PLL_B = 2


class Si5351:
    accuracy = 0.1  # Hz

    def __init__(self, address=SI5351_I2C_ADDRESS_DEFAULT, busNum=1):
        self.crystalFreq = SI5351_CRYSTAL_FREQ_25MHZ
        self.crystalLoad = SI5351_CRYSTAL_LOAD_10PF
        self.crystalPPM = 30

        self.i2cAddress = address
        self.i2cBus = SMBus(busNum)

    def __del__(self):
        self.i2cBus.close()

    @staticmethod
    def setBit(v, index, x):
        """Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value."""
        mask = 1 << index  # Compute mask, an integer with just bit 'index' set.
        v &= ~mask  # Clear the bit indicated by the mask (if x is False)
        if x:
            v |= mask  # If x was True, set the bit indicated by the mask.
        return v  # Return the result, we're done.

    def setup(self, pll, output, setting, enable=True):
        self.setupPLL(pll, setting.a, setting.b, setting.c)
        self.setupMultisynth(output, pll, setting.d, setting.e, setting.f, setting.R)
        self.enableOutputs(output, enable)

    def setupPLL(self, pll, a, b=0, c=1):
        P1 = int(128 * a + np.floor(128.0 * b / c) - 512)
        P2 = int(128 * b - c * np.floor(128.0 * b / c))
        P3 = int(c)
        pll_base_address = SI5351_REGISTER_26_MULTISYNTH_NA_PARAMETERS_1 if pll == 1 else SI5351_REGISTER_26_MULTISYNTH_NA_PARAMETERS_1 + 8
        self.i2cBus.write_byte_data(self.i2cAddress, pll_base_address + 0, (P3 & 0x0000FF00) >> 8)
        self.i2cBus.write_byte_data(self.i2cAddress, pll_base_address + 1, (P3 & 0x000000FF))
        self.i2cBus.write_byte_data(self.i2cAddress, pll_base_address + 2, (P1 & 0x00030000) >> 16)
        self.i2cBus.write_byte_data(self.i2cAddress, pll_base_address + 3, (P1 & 0x0000FF00) >> 8)
        self.i2cBus.write_byte_data(self.i2cAddress, pll_base_address + 4, (P1 & 0x000000FF))
        self.i2cBus.write_byte_data(self.i2cAddress, pll_base_address + 5,
                                    ((P3 & 0x000F0000) >> 12) | ((P2 & 0x000F0000) >> 16))
        self.i2cBus.write_byte_data(self.i2cAddress, pll_base_address + 6, (P2 & 0x0000FF00) >> 8)
        self.i2cBus.write_byte_data(self.i2cAddress, pll_base_address + 7, (P2 & 0x000000FF))

        # Reset both PLLs
        self.i2cBus.write_byte_data(self.i2cAddress, SI5351_REGISTER_177_PLL_RESET, (1 << 7) | (1 << 5))
        if pll == SI5351_PLL_A:
            self.plla_freq = self.crystalFreq * (a + b / c)
        else:
            self.pllb_freq = self.crystalFreq * (a + b / c)

    def setupMultisynth(self, output, pll, d, e=0, f=1, R=1):
        if d == 4:  # Output Multisynth Divider Equations (150 MHz < Fout <= 200 MHz)
            P1 = 0
            P2 = 0
            P3 = 1
            e = 0
            R = 0
            MS0_DIVBY4 = 3
        else:  # Output Multisynth Divider Equations (Fout <= 150 MHz)
            P1 = int(128 * d + np.floor(128.0 * e / f) - 512)
            P2 = int(128 * e - f * np.floor(128.0 * e / f))
            P3 = int(f)
            R = int(np.log2(R))
            MS0_DIVBY4 = 0
        multisynth_base_address = 0
        if output == 0: multisynth_base_address = SI5351_REGISTER_42_MULTISYNTH0_PARAMETERS_1
        if output == 1: multisynth_base_address = SI5351_REGISTER_50_MULTISYNTH1_PARAMETERS_1
        if output == 2: multisynth_base_address = SI5351_REGISTER_58_MULTISYNTH2_PARAMETERS_1
        if output == 3: multisynth_base_address = SI5351_REGISTER_66_MULTISYNTH3_PARAMETERS_1
        if output == 4: multisynth_base_address = SI5351_REGISTER_74_MULTISYNTH4_PARAMETERS_1
        if output == 5: multisynth_base_address = SI5351_REGISTER_82_MULTISYNTH5_PARAMETERS_1

        self.i2cBus.write_byte_data(self.i2cAddress, multisynth_base_address + 0, (P3 & 0x0000FF00) >> 8)
        self.i2cBus.write_byte_data(self.i2cAddress, multisynth_base_address + 1, (P3 & 0x000000FF))
        self.i2cBus.write_byte_data(self.i2cAddress, multisynth_base_address + 2,
                                    ((MS0_DIVBY4 & 0x00000003) << 2) + ((R & 0x00000007) << 4) + (
                                            (P1 & 0x00030000) >> 16))
        self.i2cBus.write_byte_data(self.i2cAddress, multisynth_base_address + 3, (P1 & 0x0000FF00) >> 8)
        self.i2cBus.write_byte_data(self.i2cAddress, multisynth_base_address + 4, (P1 & 0x000000FF))
        self.i2cBus.write_byte_data(self.i2cAddress, multisynth_base_address + 5,
                                    ((P3 & 0x000F0000) >> 12) | ((P2 & 0x000F0000) >> 16))
        self.i2cBus.write_byte_data(self.i2cAddress, multisynth_base_address + 6, (P2 & 0x0000FF00) >> 8)
        self.i2cBus.write_byte_data(self.i2cAddress, multisynth_base_address + 7, (P2 & 0x000000FF))

        clkControlReg = 0x0F  # 8mA drive strength, MS0 as CLK0 source, Clock not inverted, powered up
        if pll == SI5351_PLL_B: clkControlReg |= (1 << 5)  # Uses PLLB
        if e == 0: clkControlReg |= (1 << 6)  # Integer mode
        if output == 0: self.i2cBus.write_byte_data(self.i2cAddress, SI5351_REGISTER_16_CLK0_CONTROL,
                                                    clkControlReg)
        if output == 1: self.i2cBus.write_byte_data(self.i2cAddress, SI5351_REGISTER_17_CLK1_CONTROL,
                                                    clkControlReg)
        if output == 2: self.i2cBus.write_byte_data(self.i2cAddress, SI5351_REGISTER_18_CLK2_CONTROL,
                                                    clkControlReg)
        if output == 3: self.i2cBus.write_byte_data(self.i2cAddress, SI5351_REGISTER_19_CLK3_CONTROL,
                                                    clkControlReg)
        if output == 4: self.i2cBus.write_byte_data(self.i2cAddress, SI5351_REGISTER_20_CLK4_CONTROL,
                                                    clkControlReg)
        if output == 5: self.i2cBus.write_byte_data(self.i2cAddress, SI5351_REGISTER_21_CLK5_CONTROL,
                                                    clkControlReg)
        if output == 6: self.i2cBus.write_byte_data(self.i2cAddress, SI5351_REGISTER_22_CLK6_CONTROL,
                                                    clkControlReg)
        if output == 7: self.i2cBus.write_byte_data(self.i2cAddress, SI5351_REGISTER_23_CLK7_CONTROL,
                                                    clkControlReg)

    def enableOutputs(self, output, enable=True):
        aktualni = self.i2cBus.read_byte_data(self.i2cAddress, SI5351_REGISTER_3_OUTPUT_ENABLE_CONTROL)
        nastavit = self.setBit(aktualni, output, not enable)
        self.i2cBus.write_byte_data(self.i2cAddress, SI5351_REGISTER_3_OUTPUT_ENABLE_CONTROL, nastavit)

    def get_parameters(self, f_out):
        logging.info('Finding Si6361 setting for frequency {0} MHz'.format(f_out/1e6))
        if f_out < 8192:
            logging.warning('Input frequency is out of range')
            raise ValueError('Input frequency is out of range')
        if f_out <= 1e6:
            R = 2 ** np.ceil(np.log2(500e3) - np.log2(f_out) + 1)
        else:
            R = 1
        if f_out > 200e6:
            logging.warning('Input frequency is out of range')
            raise ValueError('Input frequency is out of range')
        # First try find integer settings
        x = np.array([f_out, self.crystalFreq])
        x = x / x.min() * x.max()
        x = Fraction(int(x[0]), int(x[1]))
        x = np.array([x.numerator, x.denominator])
        x = x.astype(np.double)
        run = 1
        final_multiplier = x
        while (self.crystalFreq * final_multiplier[0]) < 600e6:
            final_multiplier = x * run
            run += 1
            if self.crystalFreq * final_multiplier[0] > 900e6:
                break
        f_vco = self.crystalFreq * final_multiplier[0]
        final_multiplier /= np.array([1, R])
        if 600e6 <= f_vco or f_vco <= 900e6:
            if 15 <= final_multiplier[0] <= 90:
                if (final_multiplier[1] == 4 or final_multiplier[1] == 6 or final_multiplier[1] >= 8) and \
                        final_multiplier[1] < 900:
                    logging.info('Integer mode')
                    logging.info('a = {}, b = {}, c = {}, d = {}, e =  {}, f = {}, R = {}'.format(final_multiplier[0], 0, 1,
                                                                                           final_multiplier[1], 0, 1,
                                                                                           R))
                    logging.info('VCO frequency is {} MHz'.format(f_vco / 1e6))
                    return SimpleNamespace(a=final_multiplier[0], b=0, c=1, d=final_multiplier[1], e=0, f=1, R=R)

        # If could not find integer setting then use fractional
        e = 0
        f = 1
        if f_out <= 112.5e6:
            for f_vco in np.linspace(SI5351_VCO_MIN_FREQ, SI5351_VCO_MAX_FREQ, int(1e3)):
                OMD = f_vco / (f_out * R)
                d = np.floor(OMD)
                if d > 2048:
                    continue
                if d < 8:
                    continue
                FMD = R * (d + e / f) * f_out / self.crystalFreq
                a = np.floor(FMD)
                c = 1048575
                b = np.round((FMD % 1) * c)
                if np.abs(f_out - self.crystalFreq * (a + b / c) / (
                        R * (d + e / f))) <= self.accuracy:  # Accuracy condition is met
                    if self.crystalFreq * (a + b / c) >= SI5351_VCO_MIN_FREQ:
                        break
        else:  # pro d=4 a d = 6
            if f_out >= 150e6:
                d = 4
            else:  # 112.5 MHz < f_out <150 MHz
                d = 6
            FMD = R * (d + e / f) * f_out / self.crystalFreq
            a = np.floor(FMD)
            c = 1048575
            b = np.round((FMD % 1) * c)
        logging.info('Fractional mode')
        logging.info('VCO frequency is {} MHz'.format(self.crystalFreq * (a + b / c) / 1e6))
        logging.info('a = {}, b = {}, c = {}, d = {}, e =  {}, f = {}, R = {}'.format(a, b, c, d, e, f, R))
        logging.info('Error of frequency {}'.format(f_out - self.crystalFreq * (a + b / c) / (R * (d + e / f))))
        if a < 15 or a > 90:
            logging.error('Value of PLL divider is out of range')
            raise Exception('Value of PLL divider is out of range')
        if b < 0 or b > 2 ** 20 - 1:
            logging.error('Value of PLL fractional numerator is out of range')
            raise Exception('Value of PLL fractional numerator is out of range')
        if d == 5 or d == 7 or d < 4 or d > 900:
            logging.error('Value of multisynth divider is out of range')
            raise Exception('Value of multisynth divider is out of range')
        if e < 0 or e > 2 ** 20 - 1:
            logging.error('Value of multisynth fractional numerator is out of range')
            raise Exception('Value of multisynth fractional numerator is out of range')
        return SimpleNamespace(a=a, b=b, c=c, d=d, e=e, f=f, R=R)


def test():
    from copy import copy
    synt = Si5351()
    # for f_out in (np.random.rand(10000)*(200e6-10e3))+10e3:
    #     print('Set frequency {} MHz.'.format(f_out/1e6))
    #     settings1 = synt.get_parameters(f_out)
    #     synt.setup(SI5351_PLL_A, 0, settings1)
    #     time.sleep(0.1)
    settings1 = synt.get_parameters(100e6)
    settings2 = copy(settings1)
    settings2.d = settings2.d*2
    print(settings1)
    print(settings2)
    # synt.setup(SI5351_PLL_A, 0, settings1)
    # synt.setup(SI5351_PLL_A, 1, settings2)
    # synt.enableOutputs(1, enable=False)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s', filename='debug.log', level=logging.DEBUG)
    test()

