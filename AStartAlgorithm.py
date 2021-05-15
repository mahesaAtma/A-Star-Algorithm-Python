import numpy as np
import pygame
import time
import os
import cv2
from win32api import GetSystemMetrics

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (GetSystemMetrics(0)//4,GetSystemMetrics(1)//5)

pygame.init()
# Ditukar karna ada perubahan, buat button
width = 500
heigh = 700
white = (255,255,255)
black = (0,0,0)
boundaries = 10
batas = width//boundaries
fonts = pygame.font.SysFont("Exo",25)

resultImage = cv2.imread("result.jpg")
resultImage = cv2.resize(resultImage,(boundaries,boundaries))
cv2.imwrite("result.jpg",resultImage)

greenImage = cv2.imread("green.jpg")
greenImage = cv2.resize(greenImage,(boundaries,boundaries))
cv2.imwrite("green.jpg",greenImage)

redImage = cv2.imread("red.jpg")
redImage = cv2.resize(redImage,(boundaries,boundaries))
cv2.imwrite("red.jpg",redImage)

blackImage = cv2.imread("black.jpg")
blackImage = cv2.resize(blackImage,(boundaries,boundaries))
cv2.imwrite("black.jpg",blackImage)

target = (np.random.randint(width-100,width)//boundaries,np.random.randint(width-100,width)//boundaries)
start = (np.random.randint(1,100)//boundaries,np.random.randint(1,100)//boundaries)

def countDistance(startx,targetx,starty,targety):
    return np.sqrt(np.abs(startx-targetx) + np.abs(starty-targety))

blackImage = pygame.image.load("black.JPG")
whiteImage = pygame.image.load("white.JPG")
resultImage = pygame.image.load("result.JPG")
greenImage = pygame.image.load("green.JPG")
redImage = pygame.image.load("red.JPG")

screen = pygame.display.set_mode((heigh,width))
screen.fill([255,255,255])
pygame.display.set_caption("A* Algoritm Visualization")


pygame.draw.rect(screen,(0,0,0),(500,0,200,500))
pygame.draw.rect(screen,(255,255,255),(520,250,100,30))
screen.blit(fonts.render("PROCESS",True,(0,0,0)),(530,260))

line = [i for i in range(0,width,boundaries)]
distance = [[100 for i in range(0,width,boundaries)] for j in range(0,width,boundaries)]
status = [[None for i in range(0,width,boundaries)] for j in range(0,width,boundaries)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.MOUSEMOTION:
        if pygame.mouse.get_pressed()[0]:
            pos = (pygame.mouse.get_pos()[0] // boundaries, pygame.mouse.get_pos()[1] // boundaries)
            if pos <= (batas,batas):
                status[pos[0]][pos[1]] = "blocked"
                screen.blit(blackImage, (pos[0] * boundaries, pos[1] * boundaries))

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
            pos2 = (pygame.mouse.get_pos()[0] // boundaries, pygame.mouse.get_pos()[1] // boundaries)
            print(pos2)
            if ((pos2 == (52,25) or pos2 == (61,27))):
                print("[ PROCESSING ] .....")
                screen.blit(resultImage, (start[0] * boundaries, start[1] * boundaries))
                screen.blit(resultImage, (target[0] * boundaries, target[1] * boundaries))
                distanceTarget = countDistance(start[0],target[0],start[1],target[1])
                status[start[0]][start[1]] = "init"
                distance[start[0]][start[1]] = distanceTarget

                while distanceTarget!=0:
                    if start[0] > 0:
                        if status[start[0]-1][start[1]] == None or status[start[0]-1][start[1]] == "open" or status[start[0]-1][start[1]] == "visited":
                            if status[start[0]-1][start[1]] != "visited":
                                status[start[0]-1][start[1]] = "open"
                                distance[start[0] - 1][start[1]] = countDistance(start[0]-1,target[0],start[1],target[1])
                                screen.blit(greenImage, ((start[0]-1) * boundaries, (start[1]) * boundaries))
                            elif status[start[0]-1][start[1]] == "visited":
                                distance[start[0] - 1][start[1]] = countDistance(start[0]-1,target[0],start[1],target[1])

                    if start[1] > 0:
                        if status[start[0]][start[1]-1] == None or status[start[0]][start[1]-1] == "open" or status[start[0]][start[1]-1] == "visited":
                            if status[start[0]][start[1]-1] != "visited":
                                status[start[0]][start[1]-1] = "open"
                                distance[start[0]][start[1]-1] = countDistance(start[0],target[0],start[1]-1,target[1])
                                screen.blit(greenImage, ((start[0]) * boundaries, (start[1]-1) * boundaries))
                            elif status[start[0]][start[1]-1] == "visited":
                                distance[start[0]][start[1]-1] = countDistance(start[0],target[0],start[1]-1,target[1])

                    if start[1] < batas:
                        if status[start[0]][start[1]+1] == None or status[start[0]][start[1]+1] == "open" or status[start[0]][start[1]+1] == "visited":
                            if status[start[0]][start[1]+1] != "visited":
                                status[start[0]][start[1]+1] = "open"
                                distance[start[0]][start[1]+1] = countDistance(start[0],target[0],start[1]+1,target[1])
                                screen.blit(greenImage, ((start[0]) * boundaries, (start[1]+1) * boundaries))
                            elif status[start[0]][start[1]+1] == "visited":
                                distance[start[0]][start[1]+1] = countDistance(start[0],target[0],start[1]+1,target[1])

                    if start[0] < batas:
                        if status[start[0]+1][start[1]] == None or status[start[0]+1][start[1]] == "open" or status[start[0]+1][start[1]] == "visited":
                            if status[start[0]+1][start[1]] != "visited":
                                status[start[0]+1][start[1]] = "open"
                                distance[start[0]+1][start[1]] = countDistance(start[0]+1,target[0],start[1],target[1])
                                screen.blit(greenImage, ((start[0]+1) * boundaries, (start[1]) * boundaries))
                            elif status[start[0] + 1][start[1]] == "visited":
                                distance[start[0]+1][start[1]] = countDistance(start[0]+1,target[0],start[1],target[1])

                    # Diagonal
                    if start[0] > 0 and start[1] > 0:
                        if status[start[0]-1][start[1]-1] == None or status[start[0]-1][start[1]-1] == "open" or status[start[0]-1][start[1]-1] == "visited":
                            if status[start[0]-1][start[1]-1] != "visited":
                                status[start[0]-1][start[1]-1] = "open"
                                distance[start[0]-1][start[1]-1] = countDistance(start[0]-1,target[0],start[1]-1,target[1])
                                screen.blit(greenImage, ((start[0]-1) * boundaries, (start[1]-1) * boundaries))
                            elif status[start[0]-1][start[1]-1] == "visited":
                                distance[start[0]-1][start[1]-1] = countDistance(start[0]-1,target[0],start[1]-1,target[1])

                    if start[0] > 0 and start[1] < batas:
                        if status[start[0]-1][start[1]+1] == None or status[start[0]-1][start[1]+1] == "open" or status[start[0]-1][start[1]+1] == "visited":
                            if status[start[0]-1][start[1]+1] != "visited":
                                status[start[0]-1][start[1]+1] = "open"
                                distance[start[0]-1][start[1]+1] = countDistance(start[0]-1,target[0],start[1]+1,target[1])
                                screen.blit(greenImage, ((start[0]-1) * boundaries, (start[1]+1) * boundaries))
                            elif status[start[0]-1][start[1]+1] == "visited":
                                distance[start[0]-1][start[1]+1] = countDistance(start[0]-1,target[0],start[1]+1,target[1])

                    if start[0] < batas and start[1] > 0:
                        if status[start[0]+1][start[1]-1] == None or status[start[0]+1][start[1]-1] == "open" or status[start[0]+1][start[1]-1] == "visited":
                            if status[start[0]+1][start[1]-1] != "visited":
                                status[start[0]+1][start[1]-1] = "open"
                                distance[start[0]+1][start[1]-1] = countDistance(start[0]+1,target[0],start[1]-1,target[1])
                                screen.blit(greenImage, ((start[0]+1) * boundaries, (start[1]-1) * boundaries))
                            elif status[start[0]+1][start[1]-1] == "visited":
                                distance[start[0]+1][start[1]-1] = countDistance(start[0]+1,target[0],start[1]-1,target[1])

                    if start[0] < batas and start[1] < batas:
                        if status[start[0]+1][start[1]+1] == None or status[start[0]+1][start[1]+1] == "open" or status[start[0]+1][start[1]+1] == "visited":
                            if status[start[0]+1][start[1]+1] != "visited":
                                status[start[0]+1][start[1]+1] = "open"
                                distance[start[0]+1][start[1]+1] = countDistance(start[0]+1,target[0],start[1]+1,target[1])
                                screen.blit(greenImage, ((start[0]+1) * boundaries, (start[1]+1) * boundaries))
                            elif status[start[0]+1][start[1]+1] == "visited":
                                distance[start[0]+1][start[1]+1] = countDistance(start[0]+1,target[0],start[1]+1,target[1])

                    minValue = 100
                    for i in range(len(distance)):
                        for j in range(len(distance)):
                            if status[i][j] != "visited" and status[i][j] != "blocked":
                                if distance[i][j] < minValue:
                                    minValue = distance[i][j]
                                    loc = (i, j)

                    distanceTarget = minValue
                    print(distanceTarget)
                    start = (loc[0],loc[1])

                    screen.blit(redImage, (loc[0] * boundaries, loc[1] * boundaries))
                    status[loc[0]][loc[1]] = "visited"
                    # pygame.time.wait(500)
                    screen.blit(resultImage, (target[0] * boundaries, target[1] * boundaries))
                    for i in line:
                        pygame.draw.line(screen, black, (0, i), (width, i))
                        pygame.draw.line(screen, black, (i, 0), (i, width))

                    pygame.draw.line(screen, black, (500, 0), (500, 500))
                    for i in distance:
                        print(i)
                    print("=============================================")
                    # for i in status:
                    #     print(i)
                    # print("=============================================")
                    time.sleep(0.5)
                    pygame.display.update()

    screen.blit(resultImage, (start[0] * boundaries, start[1] * boundaries))
    screen.blit(resultImage, (target[0] * boundaries, target[1] * boundaries))
    for i in line:
        pygame.draw.line(screen, black, (0, i), (width, i))
        pygame.draw.line(screen, black, (i, 0), (i, width))

    pygame.draw.line(screen, black, (500, 0), (500, 500))
    pygame.display.update()

for i in distance:
    print(i)
print("=============================================")
for i in status:
    print(i)
print(start,target)