# * With input "10.0.0.0", "10.0.0.50"  => return   50
# * With input "10.0.0.0", "10.0.1.0"   => return  256
# * With input "20.0.0.10", "20.0.1.0"  => return  246
# ip2bit = (a * (256*3)) + (b * (256*2)) + (c * 256)) + d + 1
# ( ip2bit[1] - ip2bit[2] ) - 1


def ips_between(start, end):
    start = [int(i) for i in start.split('.')]
    end = [int(i) for i in end.split('.')]
    ip_start = (start[0] * (256 ** 3)) + (start[1] * (256 ** 2)) + (start[2] * 256) + start[3] + 1
    ip_end = (end[0] * (256 ** 3)) + (end[1] * (256 ** 2)) + (end[2] * 256) + end[3] + 1
    return (ip_end - ip_start)


print(ips_between("10.0.0.0", "10.1.1.0"))
