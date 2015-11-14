class Transition(object):
    """
    This class defines a set of transitions which are applied to a
    configuration to get the next configuration.
    """
    # Define set of transitions
    LEFT_ARC = 'LEFTARC'
    RIGHT_ARC = 'RIGHTARC'
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'

    def __init__(self):
        raise ValueError('Do not construct this object!')

    @staticmethod
    def left_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
            """
        if not conf.buffer or not conf.stack:
            return -1
        temp = []
        for arc in conf.arcs:  # Pull out all dependent words in to the temp list
            temp.append(arc[-1])

        idx_wi = conf.stack[-1]
        vdo = 0
        if len(temp) == 0 and idx_wi != 0:
            vdo = 1
        elif not (idx_wi in temp) and idx_wi != 0 and len(temp) > 0:
            vdo = 1

        if (vdo == 1):
            idx_wj = conf.buffer[0]
            conf.stack.pop()
            conf.arcs.append((idx_wj, relation, idx_wi))

        else:
            return -1

    @staticmethod
    def right_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer or not conf.stack:
            return -1

        # You get this one for free! Use it as an example.

        s = conf.stack[-1]
        b = conf.buffer.pop(0)

        conf.stack.append(b)
        conf.arcs.append((s, relation, b))

    @staticmethod
    def reduce(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.stack:
            return -1

        temp = []

        for arc in conf.arcs:
            temp.append(arc[-1])

        idx_wi = conf.stack[-1]

        if idx_wi in temp:
            conf.stack.pop()
        else:
            return -1

    @staticmethod
    def shift(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer:
            return -1

        idx_wj = conf.buffer.pop(0)
        conf.stack.append(idx_wj)
