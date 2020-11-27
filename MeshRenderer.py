# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 13:25:10 2020

@author: VISAL
"""
from constants import *
from OpenGL.GL import *
from OpenGL.GLU import *

def CubeMesh():
    glBegin(GL_QUADS)
    for face in cube_faces_vector4:
        x = 0
        for vertex in face:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(cube_vertices_vector3[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in cube_edges_vector2:
        for vertex in edge:
            glVertex3fv(cube_vertices_vector3[vertex])
    glEnd()
    
def ChairMesh():
    glBegin(GL_QUADS)
    for face in chair_faces_vector4:
        x = 0
        for vertex in face:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(chair_vertices_vector3[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in chair_edges_vector2:
        for vertex in edge:
            glVertex3fv(chair_vertices_vector3[vertex])
    glEnd()
    
    
    
