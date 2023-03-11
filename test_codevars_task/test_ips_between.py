from code_vars_task.Ip_between import ips_between


class TestIpsBetween:

    def test_izi(self):
        assert ips_between('20.0.0.10', '20.0.1.0') == 246
        assert ips_between("10.0.0.0", "10.0.1.0") == 256
        assert ips_between("10.0.0.0", "10.0.0.50") == 50
        assert ips_between('46.90.238.149', '46.114.134.29') == 1546120
