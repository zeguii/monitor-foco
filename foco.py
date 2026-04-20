import cv2
import mediapipe as mp
import time

mp_rosto = mp.solutions.face_mesh
rosto = mp_rosto.FaceMesh(max_num_faces=1, refine_landmarks=False)

camera = cv2.VideoCapture(0)
inicio_distracao = 0

while True:
    sucesso, frame = camera.read()
    if not sucesso:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = rosto.process(frame_rgb)

    if resultado.multi_face_landmarks:
        pontos = resultado.multi_face_landmarks[0].landmark
        
        topo_cabeca = pontos[10].y
        nariz = pontos[1].y
        queixo = pontos[152].y
        
        distancia_cima = nariz - topo_cabeca
        distancia_baixo = queixo - nariz
        
        proporcao = distancia_baixo / distancia_cima if distancia_cima > 0 else 1
        
        if proporcao < 0.65:
            if inicio_distracao == 0:
                inicio_distracao = time.time()
            
            tempo_distraido = time.time() - inicio_distracao
            
            if tempo_distraido > 3:
                cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), -1)
                cv2.putText(frame, "SOLTA O CELULAR!", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
        else:
            inicio_distracao = 0

    cv2.imshow("Monitor de Foco", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()