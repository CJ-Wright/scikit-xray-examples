__author__ = 'christopher'

from dataportal import DataBroker as db
from dataportal.broker.simple_broker import EventQueue
import numpy as np
import matplotlib.pyplot as plt

plt.ion()

hdr = db[-1]
queue = EventQueue(hdr)

data = np.zeros()
calib_dict = {}
while True:
    queue.update()
    new_events = queue.get()
    # sum the new events into the previous events
    # mask pixels
    # plt.imshow(summed), plt.colorbar()
    # convert from pixel to I(Q)
    # plt.plot(Q, raw_iq)
    # plt.show()
    # generate raw I(Q) error
    # plt.plot(Q, raw_iq_error)
    # plt.show()
    # subtract background from raw I(Q)
    # propagate raw I(Q) and background I(Q) error to I(Q)
    # plt.plot(Q, iq)
    # plt.show()
    # propagate the S(Q) error
    # plot total G(r) bounding box

