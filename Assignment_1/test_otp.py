import unittest
import otp_V1

class TestOtp(unittest.TestCase):
    def test_email(self):
        self.assertIn("@",otp_V1.userEmail,"Invalid Email")
        self.assertIn(".com",otp_V1.userEmail, "Invalid Email")
    def test_otpLength(self):
        otp = otp_V1.generateOtp
        self.assertGreaterEqual(len(otp),6,"Length of otp should be greater or equal to 6")
if __name__ == '__main__':
   unittest.main()


