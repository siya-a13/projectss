---
longform:
  format: single
  title: Gossip
title: Gossip
---
![[Gossip.jpg]]

## **Working steps of Gossip protocol :**

-  Initially, To receive endpoint state information, it will be done when Cassandra starts up, it registers itself with the Gossiper.

- After that, Periodically, typically once per second then Gossiper will choose the random node in a ring to start a Gossip session.

-  After that, Initiating node will send the request GossipDigestSynMessage to the receiving node which simply means that it is requesting a synchronization.

-  After that, when receiving node will get the request then it will acknowledge the request with GossipDigestAckMessage message to acknowledge the request.

- Finally, when Initiating node will get the acknowledgment from receiving node then again it will send the acknowledgment with GossipDigestAck2Message.
