class Patient:
    def __init__(self,patient_id, name, condition):
        self.id = patient_id
        self.name = name
        self.condition = condition
        self.next_patient = None


class PatientsList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_patient(self, patient_id, name, condition):
        new_patient = Patient(patient_id, name, condition)
        if not self.head:
            self.head = new_patient

        if not self.tail:
            self.tail = new_patient
        else:
            self.tail.next_patient = new_patient
            self.tail = new_patient
        
    def remove_patient(self, patient_id):
        if not self.head:
            print("Nenhum paciente na lista!")
        else:    
            current_node = self.head
            if self.head.id == patient_id:
                if self.head.next_patient:
                    self.head = self.head.next_patient
                else:
                    self.head = None
                    self.tail = None
            else:    
                while current_node.id != patient_id:
                    previous_node = current_node
                    current_node = current_node.next_patient
                if current_node.next_patient:
                    previous_node.next_patient = current_node.next_patient
                else:
                    previous_node.next_patient = None
                    self.tail = previous_node
            # previous_node.next_patient = current_node.next_patient if current_node.next_patient else None

    def list_all_patients(self):
        if self.head:
            current_node = self.head
            print(f"\nHead --> {self.head.name}")
            print(f"Tail --> {self.tail.name}")
            print("Lista de pacientes:")
            while current_node != None:
                print(f"{current_node.id} \t {current_node.name} \t {current_node.condition}")
                current_node = current_node.next_patient
                
        else:
            print("Nenhum paciente na lista.")


def main():
    try:
        patients_list = PatientsList()
        # list
        patients_list.list_all_patients()
        # add
        patients_list.add_patient("1","Eduardo","Em análise")
        patients_list.add_patient("2","Vitor","Em tratamento intensivo")
        patients_list.add_patient("3","Jean","Em estado crítico")
        # list
        patients_list.list_all_patients()
        # remove
        patients_list.remove_patient("2")
        # list
        patients_list.list_all_patients()

    except Exception as e:
        print(f"Erro: {e}")

main()