!pip install qiskit
!pip install pylatexenc
!pip install qiskit-aer

from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit.quantum_info.operators import Operator

#演習１
q = QuantumRegister(1, 'q')
cir1 = QuantumCircuit(q)
cir1.h(q[0])
cir1.draw('mpl')

#演習２ 行列表現
Operator(cir1)

#演習３　観測
c = ClassicalRegister(1, 'c')
meas1 = QuantumCircuit(q, c)
meas1.barrier(q)
meas1.measure(q, c)
qc1 = cir1.compose(meas1)
qc1.draw('mpl')

#演習３　観測回数表示
backend_sim = AerSimulator()
job_sim = backend_sim.run(qc1, shots=1024)
result_sim = job_sim.result()
counts = result_sim.get_counts(qc1)
print(counts)
plot_histogram(counts)

#演習４　回路の作成
q = QuantumRegister(2, 'q')
cir2 = QuantumCircuit(q)
cir2.h(q[0])
cir2.cx(q[0], q[1])
cir2.draw('mpl')

#演習４　行列表現
Operator(cir2)

#演習５　観測
c = ClassicalRegister(2, 'c')
meas2 = QuantumCircuit(q, c)
meas2.barrier(q)
meas2.measure(q, c)
qc2 = cir2.compose(meas2)
qc2.draw('mpl')

#演習５　観測回数表示
backend_sim = AerSimulator()
job_sim = backend_sim.run(qc2, shots=1024)
result_sim = job_sim.result()
counts = result_sim.get_counts(qc2)
print(counts)
plot_histogram(counts)