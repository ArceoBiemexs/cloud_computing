import streamlit as st
import random
import time
import json
import threading
import numpy as np
import math

ei = []
ai = []
R = 0
gamma = 0.75
alpha = 0.9
# Inicialización de los valores Q
Q = np.array(np.zeros([101, 21]))
iterator = 0
action = 24
current_temp = 30
start = 0
key = 1


class Q_learning(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print('Q_Learning')

    # modelo para entrenamiento
    def respond(self, Yk, Uk):
        return (Uk) + (Yk - (Uk)) * math.exp(-1.0/3.0)

    # Definición de los estados
    def estados(self):
        Y = 20.0
        estados = []
        for k in range(101):
            Y = round(Y, 1)
            estados.append(Y)
            Y = Y + 0.1
        return estados

    # Definición de las acciones
    def acciones(self):
        A = 20.0
        acciones = []
        for k in range(21):
            A = round(A, 1)
            acciones.append(A)
            A = A + 0.5
        return acciones

    # Definición de las recompensas
    def reward(self, temp):
        if 23.5 < temp < 24.5:
            return 1.0
        else:
            return 0.0

    def Ambiente(self, ei, ai):
        y = self.respond(ei, ai)
        R_i1 = self.reward(y)
        return y, R_i1

    def run(self):
        global ei, ai, Q, start, gamma, alpha
        ei = self.estados()
        ai = self.acciones()
        # Implementación del proceso de Q-Learning
        for i in range(100000):
            estado_actual = np.random.randint(0, 101)
            accion_realizable = np.random.randint(0, 21)
            temp_siguiente, Ri = self.Ambiente(ei[estado_actual], ai[accion_realizable])
            if temp_siguiente > 30.0:
                temp_siguiente = 30.0
            if temp_siguiente < 20.0:
                temp_siguiente = 20.0
            estado_siguiente = ei.index(round(temp_siguiente, 1))
            TD = Ri + gamma * Q[estado_siguiente, np.argmax(Q[estado_siguiente,])] - Q[estado_actual, accion_realizable]
            Q[estado_actual, accion_realizable] = Q[estado_actual, accion_realizable] + alpha * TD
        start = 1
        print('Q ', Q)


class Leer_Sensor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print('Inicializado Sensor...')
        self.running = True

    def work(self):
        global current_temp
        try:
            # Simula la lectura del sensor
            current_temp = 20.0 + 10.0 * random.random()
            time.sleep(1)
        except Exception as e:
            print(e)

    def run(self):
        while self.running:
            self.work()


class Control(threading.Thread):
    def __init__(self):
        global key, start, current_temp, ei, ai, Q
        threading.Thread.__init__(self)
        print('iniciando Control')
        self.running = True

    def run(self):
        global key, start, current_temp, ei, ai, Q
        while self.running:
            time.sleep(1)
            print('start pub ', start)
            try:
                if start == 1:
                    estado_act = ei.index(round(current_temp, 1))
                    acc_sig = np.argmax(Q[estado_act, ])
                    action = ai[acc_sig]
                    val = {
                        "id": key,
                        "valor": action
                    }
                    json_datos = json.dumps(val)
                    print(json_datos)
                    key = 0
            except Exception as e:
                print(e)


def main():
    global current_temp

    st.title("Q-Learning with Streamlit")

    if 'qlearning' not in st.session_state:
        st.session_state.qlearning = Q_learning()
        st.session_state.qlearning.start()

    if 'sensor' not in st.session_state:
        st.session_state.sensor = Leer_Sensor()
        st.session_state.sensor.start()

    if 'control' not in st.session_state:
        st.session_state.control = Control()
        st.session_state.control.start()

    st.write("Q-Learning is running...")
    st.write(f"Current Temperature: {current_temp}")

    # Stop threads when the app is closed
    if st.button("Stop"):
        st.session_state.qlearning.running = False
        st.session_state.sensor.running = False
        st.session_state.control.running = False


if __name__ == "__main__":
    main()
