# postcodes generator
# TASK: takes 2 strings: '67-600' and '82-900' and returns a list of codes between


def main():
    x = '67-600'
    y = '82-900'
    c = []
    c.insert(0, x)
    c.insert(len(c), y)
    a = (len(c))

    def add_new(z):
        return c.insert((a-1), z)
    # below examples
    add_new('79-901')
    print(c)
    add_new('45-444')
    print(c)
    add_new('45-443')
    print(c)
    add_new('88-443')
    print(c)
    add_new('45-423')
    print(c)
    add_new('11-111')
    print(c)
    add_new('22-222')
    print(c)

if __name__ == '__main__':
    main()


