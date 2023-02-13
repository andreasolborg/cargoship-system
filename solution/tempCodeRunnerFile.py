olding_container = []
        for section in self.get_sections():
                for stacks in section.get_container_stacks():
                    for containers in stacks.get_containers():
                        for container in containers:
                            if container.get_code() == container_code:
                                print("Container "+ container.get_code() + " found in section " + str(section.get_sectionID()) + " stack " + str(stacks.get_location_in_section()) + " container " + str(containers.index(container)+1), "(means the container is the " + str(containers.index(container)+1) + "th container in the stack)")
                                return container