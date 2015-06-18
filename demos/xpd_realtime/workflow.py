__author__ = 'christopher'

from dataportal import DataBroker as db
from dataportal.broker.simple_broker import EventQueue
hdr = db[-1]
queue = EventQueue(hdr)
while True:
    queue.update()
    new_events = queue.get()
    # do stuff with the events
    time.sleep(1)