import ptvsd
ptvsd.enable_attach(secret = 'secret')
ptvsd.wait_for_attach()