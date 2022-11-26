import pygame
import random
import gc
from vars import *
import time


class Node:

    count = 0

    def __init__(self, parent,leftChild, rightChild):
        
       Node.count +=1
       self.id = Node.count

       self.parent = parent
       self.leftChild = leftChild
       self.rightChild = rightChild
       self.value = None
       self.position = (None, None)
       self.path = None


# Affichage de l'arbre
def draw_child(node, p, level):

    if (p == 1):  #fils gauche

        node.position = node.parent.position[0] - (400/(level**2)), node.parent.position[1]+150
        pygame.draw.circle(window,NODE_COLOR,node.position,15)
        pygame.draw.line(window,NODE_COLOR,node.parent.position,node.position)

    elif (p == 0): #fils droit

        node.position = node.parent.position[0] + (400/(level**2)), node.parent.position[1]+150
        pygame.draw.circle(window,NODE_COLOR,node.position,15)
        pygame.draw.line(window,NODE_COLOR,node.parent.position,node.position)

    if (node.leftChild is not None):
        draw_child(node.leftChild, 1, level+1)

    if (node.rightChild is not None):
        draw_child(node.rightChild, 0, level+1)

def Draw_Tree(node):

        node.position = (Width/2,200)

        size = 15
        pygame.draw.circle(window,NODE_COLOR,node.position,size)

        draw_child(node.leftChild, 1, 1)
        draw_child(node.rightChild, 0, 1)

        for obj in gc.get_objects():
            if isinstance(obj, Node):
                if obj.leftChild is None and obj.rightChild is None:
                    font = pygame.font.Font('assets/Poppins-Medium.ttf', 15)
                    text = font.render(str(obj.value), True, NODE_COLOR, BG_Color)
                    textRect = text.get_rect()
                    textRect.center = (obj.position[0], obj.position[1]+50)
                    window.blit(text, textRect)

# Creation de L'arbre
def creat_Node(parent, i):
    if i !=0 :
        Node_ = Node(parent,None,None)
        Node_.leftChild = creat_Node(Node_,i-1)
        Node_.rightChild = creat_Node(Node_,i-1)
        return Node_
    else:
        Node_ = Node(parent,None,None)
        Node_.value = random.randint(-100, 100)
        return Node_

def creat_tree():
        initial_Node = Node(None,None,None)
        initial_Node.leftChild =   creat_Node(initial_Node,3)
        initial_Node.rightChild =  creat_Node(initial_Node,3)

        return initial_Node

# Algorithme MINIMAX
def MinMax(node, player, depth = 5):
    if depth == 1 :

        pygame.draw.circle(window,EXPLORED_NODE,node.position,15)

        font = pygame.font.Font('assets/Poppins-Medium.ttf', 15)
        text = font.render(str(node.value), True, BG_Color, EXPLORED_NODE)
        textRect = text.get_rect()
        textRect.center = (node.position[0], node.position[1])
        window.blit(text, textRect)

        time.sleep(0.2)
        pygame.display.flip()
        # Display the current node’s value and mark it as exploNODE_COLOR
    else :

        pygame.draw.circle(window,EXPLORED_NODE,node.position,15)
        time.sleep(0.2)
        pygame.display.flip()

        # mark the current node as explored NODE_COLOR
        listChildren = [node.leftChild,node.rightChild]
        # player = +1 ---> Max
        if player == 1 :
            bestValue = float('-inf')
            bestPath = None

            for child in listChildren:

                pygame.draw.circle(window,EXPLORED_NODE,child.position,15)
                pygame.draw.line(window,EXPLORED_NODE,node.position,child.position)
                time.sleep(0.2)
                pygame.display.flip()

                MinMax(child ,-player ,depth-1)

                if child.value > bestValue:
                    bestValue = child.value
                    bestPath = child

        # player = -1 ---> Min
        else :
            bestValue = float('inf')
            bestPath = None

            for child in listChildren:

                pygame.draw.circle(window,EXPLORED_NODE,node.position,15)
                pygame.draw.line(window,EXPLORED_NODE,node.position,child.position)
                time.sleep(0.2)
                pygame.display.flip()

                MinMax(child, -player ,depth-1)
                if child.value < bestValue:
                    bestValue = child.value
                    bestPath = child

        node.value = bestValue
        node.path = bestPath
            
        pygame.draw.line(window,Alpha_Beta,bestPath.position,bestPath.parent.position)

        font = pygame.font.Font('assets/Poppins-Medium.ttf', 15)
        text = font.render(str(node.value), True, BG_Color, EXPLORED_NODE)
        textRect = text.get_rect()
        textRect.center = (node.position[0], node.position[1])
        window.blit(text, textRect)

        time.sleep(0.2)
        pygame.display.flip()

# Algorithme NegaMax

def NegaMax(node, player, depth = 5):
    if depth == 1 :
        if player == -1:
            node.value = -node.value

        pygame.draw.circle(window,EXPLORED_NODE,node.position,15)

        font = pygame.font.Font('assets/Poppins-Medium.ttf', 15)
        text = font.render(str(node.value), True, BG_Color, EXPLORED_NODE)
        textRect = text.get_rect()
        textRect.center = (node.position[0], node.position[1])
        window.blit(text, textRect)

        time.sleep(0.2)
        pygame.display.flip()

    
    else:
        pygame.draw.circle(window,EXPLORED_NODE,node.position,15)

        time.sleep(0.2)
        pygame.display.flip()

        listChildren = [node.leftChild, node.rightChild]
        bestValue = float('-inf')
        bestPath = None

        for child in listChildren:

            # mark child and link
            pygame.draw.circle(window,EXPLORED_NODE,child.position,15)
            pygame.draw.line(window,EXPLORED_NODE,node.position,child.position)

            time.sleep(0.2)
            pygame.display.flip()

            NegaMax(child, -player, depth-1)
            child.value = -child.value

            if child.value > bestValue :
                bestValue = child.value
                bestPath = child
    
        node.value = bestValue
        node.path = bestPath
        # display value and best path

        # pygame.draw.circle(window,Alpha_Beta,bestPath.position,15)
        pygame.draw.line(window,Alpha_Beta,bestPath.position,bestPath.parent.position)

        font = pygame.font.Font('assets/Poppins-Medium.ttf', 15)
        text = font.render(str(node.value), True, BG_Color, EXPLORED_NODE)
        textRect = text.get_rect()
        textRect.center = (node.position[0], node.position[1])
        window.blit(text, textRect)

        time.sleep(0.2)
        pygame.display.flip()

# Algorithme NegaMax alpha-beta Pruning
def NegaMaxAlphaBetaPruning(node, player , depth = 5, alpha = float('-inf'), beta = float('inf')):

    if depth == 1 :
        if player == -1:
            node.value = -node.value

        # display node value and mark 
        pygame.draw.circle(window,EXPLORED_NODE,node.position,15)

        font = pygame.font.Font('assets/Poppins-Medium.ttf', 15)
        text = font.render(str(node.value), True, BG_Color, EXPLORED_NODE)
        textRect = text.get_rect()
        textRect.center = (node.position[0], node.position[1])
        window.blit(text, textRect)

        # display aplha beta

        pygame.draw.rect(window, BG_Color, pygame.Rect(node.position[0]-15, node.position[1]-60, 30, 40))


        font = pygame.font.Font('assets/Poppins-Medium.ttf', 15)
        text = font.render(str(alpha), True,Alpha_Beta, BG_Color)
        textRect = text.get_rect()
        textRect.center = (node.position[0], node.position[1]-50)
        window.blit(text, textRect)

        font = pygame.font.Font('assets/Poppins-Medium.ttf', 15)
        text = font.render(str(beta), True,Alpha_Beta, BG_Color)
        textRect = text.get_rect()
        textRect.center = (node.position[0], node.position[1]-25)
        window.blit(text, textRect)

        time.sleep(0.2)
        pygame.display.flip()

    else :
        # mark the node 
        pygame.draw.circle(window,EXPLORED_NODE,node.position,15)

        # display alpha beta

        pygame.draw.rect(window, BG_Color, pygame.Rect(node.position[0]-15, node.position[1]-60, 30, 40))

        font = pygame.font.Font('assets/Poppins-Medium.ttf', 15)
        text = font.render(str(alpha), True,Alpha_Beta, BG_Color)
        textRect = text.get_rect()
        textRect.center = (node.position[0], node.position[1]-50)
        window.blit(text, textRect)

        font = pygame.font.Font('assets/Poppins-Medium.ttf', 15)
        text = font.render(str(beta), True,Alpha_Beta, BG_Color)
        textRect = text.get_rect()
        textRect.center = (node.position[0], node.position[1]-25)
        window.blit(text, textRect)


        time.sleep(0.2)
        pygame.display.flip()


        listChildren = [node.leftChild, node.rightChild]
        bestValue = float('-inf')
        bestPath = None

        for child in listChildren:
            # mark link and node
            pygame.draw.circle(window,EXPLORED_NODE,child.position,15)
            pygame.draw.line(window,EXPLORED_NODE,node.position,child.position)

            time.sleep(0.2)
            pygame.display.flip()

            NegaMaxAlphaBetaPruning(child, -player, depth-1, -beta, -alpha)
            child.value = -child.value
            
            if child.value > bestValue:
                bestValue = child.value
                bestPath = child
            
            if bestValue > alpha :
                alpha = bestValue
                # display new value of alpha
                
                pygame.draw.rect(window, BG_Color, pygame.Rect(node.position[0]-15, node.position[1]-60, 30, 40))

                font = pygame.font.Font('assets/Poppins-Medium.ttf', 15)
                text = font.render(str(alpha), True,Alpha_Beta, BG_Color)
                textRect = text.get_rect()
                textRect.center = (node.position[0], node.position[1]-50)
                window.blit(text, textRect)

                font = pygame.font.Font('assets/Poppins-Medium.ttf', 15)
                text = font.render(str(beta), True,Alpha_Beta, BG_Color)
                textRect = text.get_rect()
                textRect.center = (node.position[0], node.position[1]-25)
                window.blit(text, textRect)

                time.sleep(0.2)
                pygame.display.flip

            if beta <= alpha :
                break
        node.value = bestValue
        node.path = bestPath

        # display best path and curent node value
        
        # pygame.draw.circle(window,Alpha_Beta,bestPath.position,15)
        pygame.draw.line(window,Alpha_Beta,bestPath.position,bestPath.parent.position)

        font = pygame.font.Font('assets/Poppins-Medium.ttf', 15)
        text = font.render(str(node.value), True, BG_Color, EXPLORED_NODE)
        textRect = text.get_rect()
        textRect.center = (node.position[0], node.position[1])
        window.blit(text, textRect)

        time.sleep(0.2)
        pygame.display.flip()
