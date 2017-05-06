import collections

#The donors that the patients prefer
preferred_rankings_patients = {
    'P1':   ['D1', 'D2', 'D3', 'D4'],
    'P2':   ['D2', 'D1', 'D4', 'D3'],
    'P3':   ['D2', 'D4', 'D3', 'D1'],
    'P4':   ['D1', 'D2', 'D3', 'D4']
}

#The patients that the donors prefer
preferred_rankings_donors = {
    'D1':    ['P1', 'P3', 'P2', 'P4'],
    'D2':    ['P1', 'P3', 'P4', 'P2'],
    'D3':    ['P4', 'P2', 'P1', 'P3'],
    'D4':    ['P1', 'P2', 'P4', 'P3']
}

#Keep track of the patients and donors who match each other
tentative_partners   = []

#Patients who are still to find a donor
free_patients                = []

def init_free_patients():
    '''Initialize the arrays of donors and patients to represent
        that they're all initially free and not matched yet'''
    for patient in preferred_rankings_patients.keys():
        free_patients.append(patient)

def begin_matching(patient):
    '''Find the first free donor available to a patient at
        any given time'''

    print("\nDEALING WITH %s\n"%(patient))
    for donor in preferred_rankings_patients[patient]:

        #Boolean for whether donor is already donating or not
        taken_match = [pair for pair in tentative_partners if donor in pair]

        if (len(taken_match) == 0):
            #tentatively match the patient and donor
            tentative_partners.append([patient, donor])
            free_patients.remove(patient)
            print('%s is no longer a free patient and is now tentatively taking blood from %s'%(patient, donor))
            break

        elif (len(taken_match) > 0):
            print('%s is donating already and is not free'%(donor))

            #Check ranking of the current patient and the ranking of the 'to-be' patient
            current_patient = preferred_rankings_donors[donor].index(taken_match[0][0])
            potential_patient = preferred_rankings_donors[donor].index(patient)

            if (current_patient < potential_patient):
                print('%s is already donating to %s'%(donor, taken_match[0][0]))
            else:
                print('%s patient is a better match than %s'%(patient, taken_match[0][0]))
                print('Making %s free again.. and tentatively patient %s is taking blood from %s'%(taken_match[0][0], patient, donor))

                #The new patient is finds a donor
                free_patients.remove(patient)

                #The old patient is again without a donor
                free_patients.append(taken_match[0][0])

                #Update the matching patient of the donor
                taken_match[0][0] = patient
                break

def stable_matching():
    '''Matching algorithm until stable match terminates'''
    while (len(free_patients) > 0):
        for patient in free_patients:
            begin_matching(patient)


def main():
    init_free_patients()
    print(free_patients)
    stable_matching()
    print('\nThe finally matched set of patients and donors\n')
    print(tentative_partners)

main()
