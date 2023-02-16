        if len(self.containers) == 0:
            raise Exception("Stack is empty")
        else:
            for index, stack in enumerate(self.containers):
                if container in stack:
                    self.containers.pop(index)
                    for c in stack:
                        self.stack_weight -= c.get_total_weight()
                        self.operationCounter += 1
                    self.update_top_weight()
                    return stack
            raise Exception("Container not found in stack")