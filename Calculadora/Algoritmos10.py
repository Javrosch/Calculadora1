def Catalan(n):
    if n == 0:
        return 1
    else:
        catalina = 4 * n - 2
        caty = catalina / (n + 1)
        return caty * Catalan(n - 1)
    
def Hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * Hanoi(n - 1) + 1
    
def DobFact(n):
	if  n == 0 or n == 1:
		return 1
	else:
		return n * DobFact(n-2)	
     
def Criba(n):
    ListaPrimo = [0] * (n - 1)
    for i in range(2, n + 1):
        ListaPrimo[i - 2] = i
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            if ListaPrimo[j - 2] != 0 and ListaPrimo[j - 2] % i == 0 and ListaPrimo[j - 2] != i:
                ListaPrimo[j - 2] = 0
    print("Los numeros primos hasta", n, "son:")
    for i in range(0, n - 1):
        if ListaPrimo[i] != 0:
            print(ListaPrimo[i])
    return ListaPrimo

def Area_poligono(Lado, NumLados):
    import numpy
    from math import tan
    angulo = numpy.pi / NumLados
    apotema = Lado / (2 * (tan(angulo)))
    area = (NumLados * Lado * apotema) / 2
    return area

def Armstrong(n):
    suma = 0
    ListaDigitos = []
    while n > 0:
        digito = n % 10
        ListaDigitos.append(digito)
        n = n // 10
    num_digitos = len(ListaDigitos)
    for digito in ListaDigitos:
        suma += digito ** num_digitos
    if suma == 0:
        return True
    else:
        return False
    
def Esperanza():
    valores_posibles = []
    probabilidades = []
    while True:
        valor = input("Ingrese un valor para el evento posible (o 'fin' para terminar): ")
        if valor.lower() == 'fin':
            break
        try:
            valor_num = int(valor)
            valores_posibles.append(valor_num)
            probabilidad = input(f"Ingrese la probabilidad asociada a {valor} (entre 0 y 1): ")
            try:
                prob = float(probabilidad)
                if 0 <= prob <= 1:
                    probabilidades.append(prob)
                else:
                    print("Probabilidad inválida. Debe estar entre 0 y 1.")
                    valores_posibles.pop()  # eliminar el valor si la probabilidad es inválida
            except ValueError:
                print("Probabilidad inválida. Por favor, ingrese un número.")
                valores_posibles.pop()  # eliminar el valor si la probabilidad es inválida
        except ValueError:
            print("Valor inválido. Por favor, ingrese un número.")

    if len(valores_posibles) != len(probabilidades):
        print("Error: La cantidad de valores y probabilidades no coincide.")
        return None

    if abs(sum(probabilidades) - 1) > 0.0001:
        print("Error: La suma de las probabilidades no es igual a 1.")
        return None

    esperanza = sum([valor * prob for valor, prob in zip(valores_posibles, probabilidades)])
    return esperanza

def Determinant_Gauss(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        raise ValueError("Matrix must be square")

    # Work on a copy to avoid modifying the original matrix
    A = [row[:] for row in matrix]
    swap_count = 0

    for k in range(n):
        # k is the pivot column/row index

        # 1. Find Best Pivot (for stability and non-zero check)
        max_row = k
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[max_row][k]):
                max_row = i

        if A[max_row][k] == 0:
            # Determinant is 0 if a pivot is 0 and no non-zero element is below it.
            # (or if the whole column is zero after initial checks)
            return 0

        # Swap rows if necessary
        if max_row != k:
            A[k], A[max_row] = A[max_row], A[k]
            swap_count += 1

        # 2. Eliminate Below the Pivot
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            # Apply the row operation across the row
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]

    # 3. Calculate Final Determinant
    determinant = 1.0
    for i in range(n):
        determinant *= A[i][i]
    if swap_count % 2 != 0:
        determinant *= -1

    return determinant

def FourMeans(data_list):
    n = len(data_list)
    if n == 0:
        return {
            'Medias': [],
            'Max': None,
            'Min': None
        }

    sum_val = 0.0  
    mult_val = 1.0  
    arm_sum_inv = 0.0  
    cuad_sum_sq = 0.0  

    for x in data_list:
        
        sum_val += x
        cuad_sum_sq += x**2

        if x <= 0:
            mult_val = 0.0
        if mult_val != 0.0:
            mult_val *= x

        
        if x == 0:
            arm_sum_inv = float('inf')
            break
        arm_sum_inv += (1.0 / x)

    media_ari = sum_val / n

    
    if mult_val > 0:
        media_geo = mult_val**(1.0/n)
    else:
        media_geo = 0.0  

    
    if arm_sum_inv == float('inf') or arm_sum_inv == 0.0:
        media_arm = 0.0
    else:
        media_arm = n / arm_sum_inv

    
    med_cu = cuad_sum_sq / n
    media_cuad = med_cu**0.5


    max_val = max(data_list)
    min_val = min(data_list)

    resultados = {
        'MediaCuad': media_cuad,
        'MediaAri': media_ari,
        'MediaGeo': media_geo,
        'MediaArm': media_arm,
        'Max': max_val,
        'Min': min_val
    }

    resultados_ordenados = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))

    return resultados_ordenados

def Inverse_GaussJordan(matrix):   
    n = len(matrix)
    if n != len(matrix[0]):
        raise ValueError("Matrix must be square.")
    augmented_matrix = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(matrix)]
    for k in range(n):
        max_row = k
        for i in range(k + 1, n):
            if abs(augmented_matrix[i][k]) > abs(augmented_matrix[max_row][k]):
                max_row = i
        if augmented_matrix[max_row][k] == 0:
            return "La Matriz es Singular"
        augmented_matrix[k], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[k]
        pivot_value = augmented_matrix[k][k]
        for j in range(k, 2 * n):
            augmented_matrix[k][j] /= pivot_value
        for i in range(n):
            if i != k:
                factor = augmented_matrix[i][k]
                for j in range(k, 2 * n):
                    augmented_matrix[i][j] -= factor * augmented_matrix[k][j]
    inverse_matrix = [row[n:] for row in augmented_matrix]
    return inverse_matrix