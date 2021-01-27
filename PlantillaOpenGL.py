from OpenGL.GL import *
from glew_wish import *
import glfw
from math import * 

def dibujarCielo():
    glBegin(GL_QUADS)
    glColor3f(0.2,0.4,0.7)
    glVertex3f(-1,1,0.0)
    glVertex3f(1,1,0.0)

    glColor3f(0.8,0.4,0.1)
    glVertex3f(1,-0.2,0.0)
    glVertex3f(-1,-0.2,0.0)
    glEnd()
    
def dibujarPasto():
    #rutinas de dibujo


    glBegin(GL_QUADS)


    glColor3f(0.1,0.4,0.1)
    glVertex3f(-1,-0.2,0.0)
    glVertex3f(1,-0.2,0.0)
    glVertex3f(1,-0.7,0.0)
    glVertex3f(-1,-0.7,0.0)

    #calle
    glColor3f(0.2,0.2,0.2)
    glVertex3f(-1,-1,0.0)
    glVertex3f(1,-1,0.0)
    glVertex3f(1,-0.7,0.0)
    glVertex3f(-1,-0.7,0.0)

    glColor3f(0.8,0.8,0.8)
    glVertex3f(-0.9,-0.87,0.0)
    glVertex3f(-0.4,-0.87,0.0)
    glVertex3f(-0.4,-0.9,0.0)
    glVertex3f(-0.9,-0.9,0.0)

    glVertex3f(-0.2,-0.87,0.0)
    glVertex3f(0.3,-0.87,0.0)
    glVertex3f(0.3,-0.9,0.0)
    glVertex3f(-0.2,-0.9,0.0)

    glVertex3f(0.5,-0.87,0.0)
    glVertex3f(1,-0.87,0.0)
    glVertex3f(1,-0.9,0.0)
    glVertex3f(0.5,-0.9,0.0)
     
    #entrada
    glColor3f(0.8,0.8,0.8)
    glVertex3f(-0.7,-0.35,0)
    glVertex3f(0.2,-0.35,0)
    glVertex3f(0.2,-0.7,0)
    glVertex3f(-1,-0.7,0)

    glVertex3f(0.2,-0.25,0)
    glVertex3f(0.52,-0.25,0)
    glVertex3f(0.52,-0.5,0)
    glVertex3f(0.2,-0.6,0)

    
    glEnd()

def dibujarRayosdesol():
    glBegin(GL_QUADS)
    glColor3f(0.9,0.4,0)

    glVertex3f(-1.3,0.1,0)
    glVertex3f(-0.43,0.2,0)
    glVertex3f(-0.5,-0.3,0)
    glVertex3f(-0.92,-0.3,0)

    glEnd()

def dibujarSol():
    glBegin(GL_POLYGON)
    glColor3f(0.9,0.8,0)
    for x in range(360):
        angulo = x * 3.14159 / 180
        glVertex3f(cos(angulo) * 0.2 - 0.75, sin(angulo) * 0.2 + -0.05, 0.0)
    glEnd()

def dibujarCasa():
    glBegin(GL_QUADS)
    #Base
    glColor3f(0.5,0.5,0.7)
    glVertex3f(-0.7,0.1,0)
    glVertex3f(0.2,0.1,0)
    glVertex3f(0.2,-0.35,0)
    glVertex3f(-0.7,-0.35,0)
    #basepuerta
    glColor3f(0.4,0.4,0.6)
    glVertex3f(0.2,0.1,0)
    glVertex3f(0.4,0.1,0)
    glVertex3f(0.4,-0.3,0)
    glVertex3f(0.2,-0.3,0)


    #Basederecha
    glColor3f(0.6,0.6,0.7)
    glVertex3f(0.5,0.15,0)
    glVertex3f(0.95,0.15,0)
    glVertex3f(0.95,-0.375,0)
    glVertex3f(0.5,-0.375,0)

    #Ventana
    glColor3f(1,0.8,0)
    glVertex3f(0.55,0.05,0)
    glVertex3f(0.85,0.05,0)
    glVertex3f(0.85,-0.3,0)
    glVertex3f(0.55,-0.3,0)

    #puerta
    glColor3f(0.4,0.2,0)
    glVertex3f(0.215,0,0)
    glVertex3f(0.375,0,0)
    glVertex3f(0.375,-0.3,0)
    glVertex3f(0.215,-0.3,0)

    #cochera
    glColor3f(0.5,0.3,0.1)
    glVertex3f(-0.6,0.05,0)
    glVertex3f(0.1,0.05,0)
    glVertex3f(0.1,-0.35,0)
    glVertex3f(-0.6,-0.35,0)


    glEnd()

def dibujarTecho():
    glBegin(GL_TRIANGLES)

    glColor3f(0.2,0.2,0.5)

    glVertex3f(-1,0.075,0)
    glVertex3f(0,0.2,0)
    glVertex3f(0.5,0.075,0)

    glVertex3f(-0.2,0.1,0)
    glVertex3f(0.25,0.25,0)
    glVertex3f(0.5,0.15,0)

    glVertex3f(0.05,0.15,0)
    glVertex3f(0.6,0.175,0)
    glVertex3f(0.8,0.15,0)

    glEnd()

def dibujarColumnas():
    glBegin(GL_QUADS)
    #columna
    glColor3f(0.7,0.7,0.7)
    glVertex3f(0.4,0.2,0)
    glVertex3f(0.5,0.2,0)
    glVertex3f(0.5,-0.4,0)
    glVertex3f(0.4,-0.4,0)
    #columna2
    glColor3f(0.8,0.8,0.87)
    glVertex3f(0.075,0.15,0)
    glVertex3f(0.4,0.15,0)
    glVertex3f(0.4,0.025,0)
    glVertex3f(0.075,0.025,0)

    #columna3
    glColor3f(0.1,0.1,0.1)

    glVertex3f(0.12,0.025,0)
    glVertex3f(0.15,0.025,0)
    glVertex3f(0.15,-0.4,0)
    glVertex3f(0.12,-0.4,0)

    glEnd()

def dibujarArbol():
    glBegin(GL_QUADS)
    glColor3f(0.4,0.2,0)
    glVertex3f(0.7,0.1,0)
    glVertex3f(0.8,0.1,0)
    glVertex3f(0.8,-0.6,0)
    glVertex3f(0.7,-0.6,0)

    glEnd()

def dibujarHojas():
    glBegin(GL_POLYGON)
    glColor3f(0.2,0.4,0.1)
    for x in range(360):
        angulo = x * 3.14159 / 180
        glVertex3f(cos(angulo) * 0.3 + 0.75, sin(angulo) * 0.1 + 0.1, 0.0)
    for x in range(360):
        angulo = x * 3.14159 / 180
        glVertex3f(cos(angulo) * 0.4 + 0.65, sin(angulo) * 0.2 + 0.3, 0.0)
    glEnd()

def dibujarManija():
    glBegin(GL_POLYGON)
    glColor3f(0.8,0.8,0.8)
    for x in range(360):
        angulo = x * 3.14159 / 180
        glVertex3f(cos(angulo) * 0.01 + 0.35, sin(angulo) * 0.01 + -0.18, 0.0)
    glEnd()

def dibujarNubes():
    glBegin(GL_POLYGON)
    glColor3f(0.9,0.8,0.9)
    #nube 1
    for x in range(360):
        angulo = x * 3.14159 / 180
        glVertex3f(cos(angulo) * 0.15 + 0.35, sin(angulo) * 0.05 + 0.8, 0.0)
    for x in range(360):
        angulo = x * 3.14159 / 180
        glVertex3f(cos(angulo) * 0.15 + 0.25, sin(angulo) * 0.05 + 0.7, 0.0)
    for x in range(360):
        angulo = x * 3.14159 / 180
        glVertex3f(cos(angulo) * 0.2 + 0.45, sin(angulo) * 0.07 + 0.75, 0.0)

    glEnd()
def dibujarNubes2():
    glBegin(GL_POLYGON)
    glColor3f(1,0.8,0.7)
    for x in range(360):
        angulo = x * 3.14159 / 180
        glVertex3f(cos(angulo) * 0.15 + 0.1, sin(angulo) * 0.05 + 0.6, 0.0)
    for x in range(360):
        angulo = x * 3.14159 / 180
        glVertex3f(cos(angulo) * 0.3 - 0.3, sin(angulo) * 0.05 + 0.6, 0.0)
    for x in range(360):
        angulo = x * 3.14159 / 180
        glVertex3f(cos(angulo) * 0.3 - 0.02, sin(angulo) * 0.07 + 0.5, 0.0)
    glEnd()

def dibujarNubes3():
    glBegin (GL_POLYGON)
    glColor3f(0.9, 0.8, 1)
    for x in range(360):
        angulo = x * 3.14159 / 180
        glVertex3f(cos(angulo) * 0.15 - 0.9, sin(angulo) * 0.05 + 0.95, 0.0)
    for x in range(360):
        angulo = x * 3.14159 / 180
        glVertex3f(cos(angulo) * 0.18 - 0.75, sin(angulo) * 0.05 + 0.9, 0.0)
    glEnd()

def dibujar():
    dibujarCielo()
    dibujarRayosdesol()
    dibujarSol()
    dibujarNubes()
    dibujarNubes2()
    dibujarNubes3()
    dibujarPasto()
    dibujarCasa()
    dibujarTecho()
    dibujarColumnas()
    dibujarArbol()
    dibujarHojas()
    dibujarManija()
    


def main():
    #inicia glfw
    ancho = 800
    alto = 900
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(ancho,alto,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,ancho,alto)
        #Establece color de borrado
        glClearColor(0.4,0.5,1,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()