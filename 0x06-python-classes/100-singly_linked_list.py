#!/usr/bin/python3
#!/usr/bin/python3
"""
Module 100-singly_linked_list
Defines singly linked list and node classes
Prints the entire list one node per line
"""


class Node:
    """
    Defines a node of a singly linked list of integers with private
    instance attributes and getter and setter properties for accessing
    and updating fields
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a node object with a field for an integer and a new node

        Args:
            data (int): integer (positive or negative)
            next_node (Node): pointer to a new linked list node

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Attribute:
            data (int): read-write property
        """
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Attribute:
            next_node (Node): read-write property
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list with a private instance attribute with no
    setters or getters and a public instance method that inserts a new node
    into the list
    """
    def __init__(self):
        """
        Performs a simple instantiation of a new linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct position in the list (ascending order)
        """
        new_node = Node(value)

        # Special case for empty linked list
        if self.__head is None:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Special case for head at end
        elif self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        else:
            # Locate the node before the point of insertion
            current = self.__head
            while (current.next_node is not None) and \
                  (current.next_node.data < new_node.data):
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node
            return

    def __repr__(self):
        """
        String representation of a singly linked list
        """
        string = ""
        temp = self.__head
        while temp is not None:
            string += string(temp.data)
            temp = temp.next_node

            if temp is not None:
                string += "\n"

        return string
