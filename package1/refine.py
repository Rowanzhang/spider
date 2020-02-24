class Refine():
    def __refine(self, anchors):
        l = lambda anchor: {'name': anchor['name'][0], 'number': anchor['number'][0]}
        return map(l, anchors)

    def go_refine(self, anchors):
        anchor = list(self.__refine(anchors))
        return anchor
