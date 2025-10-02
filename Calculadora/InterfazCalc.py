import tkinter as tk
from tkinter import ttk
import requests

class InterfazCalc:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.frame_catalan = tk.Frame(self.notebook)
        self.frame_hanoi = tk.Frame(self.notebook)
        self.frame_dobfact = tk.Frame(self.notebook)
        self.frame_criba = tk.Frame(self.notebook)
        self.frame_area_poligono = tk.Frame(self.notebook)
        self.frame_armstrong = tk.Frame(self.notebook)
        self.frame_esperanza = tk.Frame(self.notebook)
        self.frame_determinant = tk.Frame(self.notebook)
        self.frame_means = tk.Frame(self.notebook)
        self.frame_inverse = tk.Frame(self.notebook)
        

        self.notebook.add(self.frame_catalan, text="Catalan")
        self.notebook.add(self.frame_hanoi, text="Hanoi")
        self.notebook.add(self.frame_dobfact, text="Doble Factorial")
        self.notebook.add(self.frame_criba, text="Criba")
        self.notebook.add(self.frame_area_poligono, text="Area Poligono")
        self.notebook.add(self.frame_armstrong, text="Armstrong")
        self.notebook.add(self.frame_esperanza, text="Esperanza Matematica")
        self.notebook.add(self.frame_determinant, text="Determinante de una Matriz")
        self.notebook.add(self.frame_inverse, text="Inverso de una Matriz")
        self.notebook.add(self.frame_means, text="Distintos tipos de medias")

        self.crear_widgets_catalan()
        self.crear_widgets_hanoi()
        self.crear_widgets_dobfact()
        self.crear_widgets_criba()  
        self.crear_widgets_area_poligono()
        self.crear_widgets_armstrong()
        self.crear_widgets_esperanza()
        self.crear_widgets_determinant()
        self.crear_widgets_inverse()
        self.crear_widgets_means()

    def crear_widgets_catalan(self):
        tk.Label(self.frame_catalan, text="Ingrese un número:").pack()
        self.entry_catalan = tk.Entry(self.frame_catalan)
        self.entry_catalan.pack()
        tk.Button(self.frame_catalan, text="Calcular", command=self.calcular_catalan).pack()
        self.label_resultado_catalan = tk.Label(self.frame_catalan, text="")
        self.label_resultado_catalan.pack()

    def crear_widgets_hanoi(self):
        tk.Label(self.frame_hanoi, text="Ingrese un número:").pack()
        self.entry_hanoi = tk.Entry(self.frame_hanoi)
        self.entry_hanoi.pack()
        tk.Button(self.frame_hanoi, text="Calcular", command=self.calcular_hanoi).pack()
        self.label_resultado_hanoi = tk.Label(self.frame_hanoi, text="")
        self.label_resultado_hanoi.pack()

    def crear_widgets_dobfact(self):
        tk.Label(self.frame_dobfact, text="Ingrese un número:").pack()
        self.entry_dobfact = tk.Entry(self.frame_dobfact)
        self.entry_dobfact.pack()
        tk.Button(self.frame_dobfact, text="Calcular", command=self.calcular_dobfact).pack()
        self.label_resultado_dobfact = tk.Label(self.frame_dobfact, text="")
        self.label_resultado_dobfact.pack()

    def crear_widgets_criba(self):
        tk.Label(self.frame_criba, text="Ingrese un número:").pack()
        self.entry_criba = tk.Entry(self.frame_criba)
        self.entry_criba.pack()
        tk.Button(self.frame_criba, text="Calcular", command=self.calcular_criba).pack()
        self.label_resultado_criba = tk.Label(self.frame_criba, text="")
        self.label_resultado_criba.pack()
    
    def crear_widgets_area_poligono(self):
        tk.Label(self.frame_area_poligono, text="Ingrese el lado:").pack()
        self.entry_area_poligono_lado = tk.Entry(self.frame_area_poligono)
        self.entry_area_poligono_lado.pack()
        tk.Label(self.frame_area_poligono, text="Ingrese el número de lados:").pack()
        self.entry_area_poligono_numlados = tk.Entry(self.frame_area_poligono)
        self.entry_area_poligono_numlados.pack()
        tk.Button(self.frame_area_poligono, text="Calcular", command=self.calcular_area_poligono).pack()
        self.label_resultado_area_poligono = tk.Label(self.frame_area_poligono, text="")
        self.label_resultado_area_poligono.pack()

    def crear_widgets_armstrong(self):
        tk.Label(self.frame_armstrong, text="Ingrese un número:").pack()
        self.entry_armstrong = tk.Entry(self.frame_armstrong)
        self.entry_armstrong.pack()
        tk.Button(self.frame_armstrong, text="Calcular", command=self.calcular_armstrong).pack()
        self.label_resultado_armstrong = tk.Label(self.frame_armstrong, text="")
        self.label_resultado_armstrong.pack()

    def crear_widgets_esperanza(self):
        tk.Label(self.frame_esperanza, text="Calcular Esperanza Matemática").pack()
        tk.Label(self.frame_esperanza, text="Ingrese los valores y probabilidades separados por comas").pack()
        self.entry_valores = tk.Entry(self.frame_esperanza, width=50)
        self.entry_valores.pack()
        self.entry_probabilidades = tk.Entry(self.frame_esperanza, width=50)
        self.entry_probabilidades.pack()
        tk.Label(self.frame_esperanza, text="Valores").pack()
        tk.Label(self.frame_esperanza, text="Probabilidades").pack()
        tk.Button(self.frame_esperanza, text="Calcular", command=self.calcular_esperanza).pack()
        self.label_resultado_esperanza = tk.Label(self.frame_esperanza, text="")
        self.label_resultado_esperanza.pack()

    def crear_widgets_determinant(self): 
        tk.Label(self.frame_determinant, text="--- Determinant Calculation ---").pack(pady=5)
        tk.Label(self.frame_determinant, text="Select Matrix Size (N x N):").pack()
        self.matrix_size_var = tk.StringVar(value=3)
        ttk.Combobox(
            self.frame_determinant,
            textvariable=self.matrix_size_var,
            values=[str(n) for n in range(2, 6)],
            state='readonly'
        ).pack(pady=5)
        tk.Button(self.frame_determinant, text="Generate Input Grid", command=self.generate_matrix_grid).pack(pady=5)
        self.grid_frame = tk.Frame(self.frame_determinant)
        self.grid_frame.pack(pady=10)
        self.matrix_entries = []
        self.generate_matrix_grid()
        tk.Button(self.frame_determinant, text="Calculate Determinant", command=self.calcular_determinant).pack(pady=10)
        self.label_resultado_determinant = tk.Label(self.frame_determinant, text="")
        self.label_resultado_determinant.pack()
    def generate_matrix_grid(self):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        self.matrix_entries.clear()
        try:
            N = int(self.matrix_size_var.get())
        except ValueError:
            return
        for i in range(N):
            row_entries = []
            for j in range(N):
                entry = tk.Entry(self.grid_frame, width=5, justify='center')
                entry.grid(row=i, column=j, padx=2, pady=2)
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)

    def crear_widgets_inverse(self):
            tk.Label(self.frame_inverse, text="--- Matrix Inverse (Gauss-Jordan) ---").pack(pady=5)
            tk.Label(self.frame_inverse, text="Select Matrix Size (N x N):").pack()
            self.inverse_matrix_size_var = tk.StringVar(value=3)
            tk.OptionMenu(self.frame_inverse, self.inverse_matrix_size_var, *list(map(str, range(2, 6)))).pack(pady=5)
            tk.Button(self.frame_inverse, text="Generate Input Grid", command=self.generate_inverse_matrix_grid).pack(pady=5)
            self.inverse_grid_frame = tk.Frame(self.frame_inverse)
            self.inverse_grid_frame.pack(pady=10)
            self.inverse_matrix_entries = []
            self.generate_inverse_matrix_grid()

            tk.Button(self.frame_inverse, text="Calculate Inverse", command=self.calcular_inverse).pack(pady=10)
            self.label_resultado_inverse = tk.Label(self.frame_inverse, text="", justify=tk.LEFT)
            self.label_resultado_inverse.pack()

    def generate_inverse_matrix_grid(self):
        for widget in self.inverse_grid_frame.winfo_children():
            widget.destroy()
        self.inverse_matrix_entries.clear()
        try:
            N = int(self.inverse_matrix_size_var.get())
        except ValueError:
            return
        for i in range(N):
            row_entries = []
            for j in range(N):
                entry = tk.Entry(self.inverse_grid_frame, width=8, justify='center')
                entry.grid(row=i, column=j, padx=2, pady=2)
                row_entries.append(entry)
            self.inverse_matrix_entries.append(row_entries)
    
    def crear_widgets_means(self):
        tk.Label(self.frame_means, text="--- Calculation of Four Means ---").pack(pady=5)
        tk.Label(self.frame_means, text="Enter numbers separated by commas (e.g., 10, 2, 5, 8)").pack()
        self.entry_means = tk.Entry(self.frame_means, width=60)
        self.entry_means.pack(pady=5)
        tk.Button(self.frame_means, text="Calculate Means", command=self.mostrar_resultados).pack(pady=10)
        self.label_resultado_means = tk.Label(self.frame_means, text="", justify=tk.LEFT)
        self.label_resultado_means.pack(pady=10)
    
    def calcular_catalan(self):
        n = int(self.entry_catalan.get())
        respuesta = requests.get(f"http://localhost:8080/catalan?n={n}")
        resultado = respuesta.json()["resultado"]
        self.label_resultado_catalan.config(text=f"Resultado: {resultado}")

    def calcular_hanoi(self):
        n = int(self.entry_hanoi.get())
        respuesta = requests.get(f"http://localhost:8080/hanoi?n={n}")
        resultado = respuesta.json()["resultado"]
        self.label_resultado_hanoi.config(text=f"Resultado: {resultado}")

    def calcular_dobfact(self):
        n = int(self.entry_dobfact.get())
        respuesta = requests.get(f"http://localhost:8080/dobfact?n={n}")
        resultado = respuesta.json()["resultado"]
        self.label_resultado_dobfact.config(text=f"Resultado: {resultado}")

    def calcular_criba(self):
        n = int(self.entry_criba.get())
        respuesta = requests.get(f"http://localhost:8080/criba?n={n}")
        resultado = respuesta.json()["resultado"]
        self.label_resultado_criba.config(text=f"Resultado: {resultado}")
    
    def calcular_area_poligono(self):
        Lado = float(self.entry_area_poligono_lado.get())
        NumLados = int(self.entry_area_poligono_numlados.get())
        respuesta = requests.get(f"http://localhost:8080/poligono?n={Lado}&m={NumLados}")
        resultado = respuesta.json()["resultado"]
        self.label_resultado_area_poligono.config(text=f"Resultado: {resultado}")

    def calcular_armstrong(self):
        n = int(self.entry_armstrong.get())
        respuesta = requests.get(f"http://localhost:8080/armstrong?n={n}")
        resultado = respuesta.json()["resultado"]
        self.label_resultado_armstrong.config(text=f"Resultado: {resultado}")
    
    def calcular_esperanza(self):
        valores = list(map(int, self.entry_valores.get().split(',')))
        probabilidades = list(map(float, self.entry_probabilidades.get().split(',')))
        datos = {'valores': valores, 'probabilidades': probabilidades}
        respuesta = requests.post("http://localhost:8080/esperanza", json=datos)
        if respuesta.status_code == 200:
            resultado = respuesta.json()["esperanza"]
            self.label_resultado_esperanza.config(text=f"Esperanza Matemática: {resultado}")
        else:         
            self.label_resultado_esperanza.config(text="Error al calcular la esperanza")

    def calcular_determinant(self):
        N = int(self.matrix_size_var.get())
        matrix = []
        try:
            for i in range(N):
                row = []
                for j in range(N):
                    value = float(self.matrix_entries[i][j].get() or 0)
                    row.append(value)
                matrix.append(row)

            datos = {'matrix': matrix}
            respuesta = requests.post(f"http://localhost:8080/determinant", json=datos)

            if respuesta.status_code == 200:
                resultado = respuesta.json()["resultado"]
                self.label_resultado_determinant.config(text=f"Determinante: {resultado:.4f}")
            else:
                error_msg = respuesta.json().get('error', 'Error desconocido.')
                self.label_resultado_determinant.config(text=f"Error: {error_msg}")
        except ValueError:
            self.label_resultado_determinant.config(text="Error de formato: Asegúrese de que todos los campos son números.")
        except Exception as e:
            self.label_resultado_determinant.config(text=f"Error de conexión o cálculo: {e}")

    
    def calcular_means(self):
        input_str = self.entry_means.get()
        try:
            data_list = [float(x.strip()) for x in input_str.split(',') if x.strip()]
            if not data_list:
                return {"error": "Ingrese al menos un número."}
            datos = {'data': data_list}            
            respuesta = requests.post(f"http:localhost:8080/means", json=datos)
            if respuesta.status_code == 200:
                return respuesta.json()
            else:
                error_msg = respuesta.json().get('error', 'Error desconocido.')
                return {"error": error_msg}
        except ValueError:
            return {"error": "Error de formato: Asegúrese de que los valores son números separados por comas."}
        except Exception as e:
            return {"error": f"Error de conexión: {e}"}
    def mostrar_resultados(self):
        resultados = self.calcular_means()
        if "error" in resultados:
            self.label_resultado_means.config(text=resultados["error"])
        else:
            display_text = (
                f"Media Aritmética: {resultados['MediaAri']:.4f}\n"
                f"Media Geométrica: {resultados['MediaGeo']:.4f}\n"
                f"Media Armónica: {resultados['MediaArm']:.4f}\n"
                f"Media Cuadrática (RMS): {resultados['MediaCuad']:.4f}\n"
                f"Máximo: {resultados['Max']:.4f}\n"
                f"Mínimo: {resultados['Min']:.4f}"
            )
            self.label_resultado_means.config(text=display_text)

    def calcular_inverse(self):
        N = int(self.inverse_matrix_size_var.get())
        matrix = []
        try:
            for i in range(N):
                row = []
                for j in range(N):
                    value = float(self.inverse_matrix_entries[i][j].get() or 0)
                    row.append(value)
                matrix.append(row)
            datos = {'matrix': matrix}
            respuesta = requests.post('http://localhost:8080/inverse', json=datos)
            if respuesta.status_code == 200:
                inverse_matrix = respuesta.json()["inverse_matrix"]
                matrix_str = "Inverse Matrix:\n"
                for row in inverse_matrix:
                    matrix_str += "[ " + ", ".join(f"{x:.4f}" for x in row) + " ]\n"
                self.label_resultado_inverse.config(text=matrix_str)
            else:
                error_msg = respuesta.json().get('error', 'Error desconocido.')
                self.label_resultado_inverse.config(text=f"Error: {error_msg}")
        except ValueError:
            self.label_resultado_inverse.config(text="Error de formato: Asegúrese de que todos los campos son números.")
        except Exception as e:
            self.label_resultado_inverse.config(text=f"Error de conexión o cálculo: {e}")


    def run(self):
            self.root.mainloop()

if __name__ == "__main__":
    app = InterfazCalc()
    app.root.mainloop()

