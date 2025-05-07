# Computación Grafica: Pong Completo v1 en Python by JDRB
import pygame

# Sonidos
RutaGol     = r"""Proyectos\Pong\Recursos\Gol.mp3"""
RutaRaqueta = r"""Proyectos\Pong\Recursos\Raqueta.mp3"""
RutaRebote  = r"""Proyectos\Pong\Recursos\Rebote.mp3"""

def mostrar_menu():
    Ventana = pygame.display.set_mode((800, 600))
    fuente = pygame.font.SysFont('Arial', 48)
    titulo = fuente.render("PONG ", True, (255, 255, 255))
    boton_jugar = pygame.Rect(300, 250, 200, 50)
    boton_salir = pygame.Rect(300, 320, 200, 50)
    fuente_boton = pygame.font.SysFont('Arial', 32)

    while True:
        Ventana.fill((0, 0, 0))
        Ventana.blit(titulo, (400 - titulo.get_width() // 2, 100))
        pygame.draw.rect(Ventana, (100, 100, 255), boton_jugar)
        pygame.draw.rect(Ventana, (255, 100, 100), boton_salir)

        jugar_txt = fuente_boton.render("Jugar", True, (255, 255, 255))
        salir_txt = fuente_boton.render("Salir", True, (255, 255, 255))
        Ventana.blit(jugar_txt, (boton_jugar.x + 60, boton_jugar.y + 10))
        Ventana.blit(salir_txt, (boton_salir.x + 60, boton_salir.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(event.pos):
                    return
                if boton_salir.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        pygame.display.flip()


if __name__ == '__main__':

    pygame.init()
    mostrar_menu()
    # Colores
    Negro = (0, 0, 0)
    Blanco = (255, 255, 255)
    Tamano = (800, 600)
    PlayerAncho = 15
    PlayerAlto = 90

    Score1 = 0
    Score2 = 0
    MaxScore = 5
    fuente = pygame.font.SysFont('Arial', 36)

    pygame.mixer.init()
    SonidoGol     = pygame.mixer.Sound(RutaGol)
    SonidoRaqueta = pygame.mixer.Sound(RutaRaqueta)
    SonidoRebote  = pygame.mixer.Sound(RutaRebote)

    Ventana = pygame.display.set_mode(Tamano)
    clock = pygame.time.Clock()

    # Coordenadas y velocidad del jugador 1
    CoorPlayer1_X = 50
    CoorPlayer1_Y = 300 - 45
    player1Vel_Y = 0

    # Coordenadas y velocidad del jugador 2
    CoorPlayer2_X = 750 - PlayerAncho
    CoorPlayer2_Y = 300 - 45
    Player2Vel_Y = 0

    # Coordenadas de la pelota
    Pelota_X = 400
    Pelota_Y = 300
    PelotaVel_X = 3
    PelotaVel_Y = 3

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # Jugador 1
                if event.key == pygame.K_w:
                    player1Vel_Y = -3
                if event.key == pygame.K_s:
                    player1Vel_Y = 3
                # Jugador 2
                if event.key == pygame.K_UP:
                    Player2Vel_Y = -3
                if event.key == pygame.K_DOWN:
                    Player2Vel_Y = 3

            if event.type == pygame.KEYUP:
                # Jugador 1
                if event.key == pygame.K_w:
                    player1Vel_Y = 0
                if event.key == pygame.K_s:
                    player1Vel_Y = 0
                # Jugador 2
                if event.key == pygame.K_UP:
                    Player2Vel_Y = 0
                if event.key == pygame.K_DOWN:
                    Player2Vel_Y = 0

        if Pelota_Y > 590 or Pelota_Y < 10:
            PelotaVel_Y *= -1

        # Revisa si la pelota sale del lado derecho (Punto para Jugador 1)
        if Pelota_X > 800:
            Score1 += 1
            Pelota_X = 400
            Pelota_Y = 300
            PelotaVel_X *= -1
            PelotaVel_Y *= -1
            SonidoGol.play()

        # Revisa si la pelota sale del lado izquierdo (Punto para Jugador 2)
        if Pelota_X < 0:
            Score2 += 1
            Pelota_X = 400
            Pelota_Y = 300
            PelotaVel_X *= -1
            PelotVel_Y *= -1
            SonidoGol.play()

        # Modifica las coordenadas para dar mov. a los jugadores/ pelota
        CoorPlayer1_Y += player1Vel_Y
        CoorPlayer2_Y += Player2Vel_Y
        # Movimiento pelota
        Pelota_X += PelotaVel_X
        Pelota_Y += PelotaVel_Y

        Ventana.fill(Negro)
        # Zona de dibujo
        jugador1 = pygame.draw.rect(Ventana, Blanco, (CoorPlayer1_X, CoorPlayer1_Y, PlayerAncho, PlayerAlto))
        jugador2 = pygame.draw.rect(Ventana, Blanco, (CoorPlayer2_X, CoorPlayer2_Y, PlayerAncho, PlayerAlto))
        pelota = pygame.draw.circle(Ventana, Blanco, (Pelota_X, Pelota_Y), 10)

        texto = fuente.render(f"{Score1} - {Score2}", True, Blanco)
        Ventana.blit(texto, (Tamano[0] // 2 - texto.get_width() // 2, 20))

        # Colisiones
        if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
            PelotaVel_X *= -1
            SonidoRaqueta.play()
            
        if Score1 >= MaxScore or Score2 >= MaxScore:
            pygame.time.delay(1000)
            game_over = True

        pygame.display.flip()
        clock.tick(60)
    
    Score1 = 0
    Score2 = 0
    mostrar_menu()
    pygame.quit()