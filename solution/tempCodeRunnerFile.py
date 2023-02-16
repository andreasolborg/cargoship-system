        for container in container_set.containers:
            try:
                self.add_container(container)
            except Exception as e:
                return

        if self.is_ship_balanced(5, 10) == True:
            print("Ship is balanced")
            
        else:
            print("Ship is not balanced")