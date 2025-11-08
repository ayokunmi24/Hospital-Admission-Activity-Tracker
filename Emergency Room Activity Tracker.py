
#GLOBALS----------------------------------------------------------------------------------------

#Constants 
HOSPITAL_NAME = 'Victorino General Hospital'
OCCUPANCY_WARNING_THRESHOLD = 80
TOTAL_BEDS_PER_UNIT = 50

#Formatting variables

RPT_WIDTH = 55
indent1 = ' ' * 2

#Current inpatients
current_cardio_inpatients = 34
current_respiratory_inpatients = 11
current_ortho_inpatients = 8


#MAIN-------------------------------------------------------------------------------------------

def main():
    fn1()

    #get ER data from user
    new_patients = int(input(indent1 + 'New Patients Seen: '))
    print ()
    print (indent1 + 'Patients Admitted to a Unit')
    cardiology_admissions = int(input(indent1 + 'Enter Cardiology Admissions: '))
    respiratory_admissions = int(input(indent1 + 'Enter Respiratory Admissions: '))
    orthopedic_admissions = int(input(indent1 + 'Enter Orthopedic Admissions: '))
    print()

    #admission
    total_admitted_patients = (cardiology_admissions + respiratory_admissions +
                               orthopedic_admissions)/new_patients * 100
    total_discharged_patients = (new_patients - total_admitted_patients)/new_patients * 100

    #occupancy
    cardio_beds_occupied = current_cardio_inpatients + cardiology_admissions
    respiratory_beds_occupied = current_respiratory_inpatients + respiratory_admissions
    orthopedic_beds_occupied = current_ortho_inpatients + orthopedic_admissions

    #occupancy rates
    c_occupancy_rate = (cardio_beds_occupied / TOTAL_BEDS_PER_UNIT) * 100
    r_occupancy_rate = (respiratory_beds_occupied / TOTAL_BEDS_PER_UNIT) * 100
    o_occupancy_rate = (orthopedic_beds_occupied / TOTAL_BEDS_PER_UNIT) * 100

    #call the next functions
    fn2(total_admitted_patients, total_discharged_patients)
    fn3(cardio_beds_occupied, c_occupancy_rate,respiratory_beds_occupied, r_occupancy_rate,
        orthopedic_beds_occupied, o_occupancy_rate)

#FUNCTIONS--------------------------------------------------------------------------------------
def fn1():
    print()
    print ('*_'*28)
    print (f'{HOSPITAL_NAME:^56}')
    print (f'{"ER & Unit Occupancy Summary":^56}')
    print ('*_'*28)
    print()
    
def fn2(total_admitted_patients, total_discharged_patients):
    print (f'{'='*53:^56}')
    print (indent1 + 'ER STATS')
    print (f'{'='*53:^56}')
    print (f'{"Total Patients":>22} {"Total Patients":>22}')
    print (f'{"ADMITTED":^30} {"DISCHARGED":^14}')
    print (f'{"-"*10:>20} {"-"*10:>22}')
    print (f'{total_admitted_patients:>16.0f}%' f'{total_discharged_patients:>22.0f}%')
    
    
def fn3(cardio_beds_occupied, c_occupancy_rate,respiratory_beds_occupied, r_occupancy_rate,
        orthopedic_beds_occupied, o_occupancy_rate):
    if c_occupancy_rate >= OCCUPANCY_WARNING_THRESHOLD:
        c_warning = ' << Near Capacity!'
    else:
        c_warning = ' '

    if o_occupancy_rate >= OCCUPANCY_WARNING_THRESHOLD:
        o_warning = ' << Near Capacity!'
    else:
        o_warning = ' '
    
    if r_occupancy_rate >= OCCUPANCY_WARNING_THRESHOLD:
        r_warning = ' << Near Capacity!'
    else:
        r_warning = ' '

    #display report
    print (f'{'='*53:^56}')
    print (indent1 + 'UNIT ANALYSIS')
    print (f'{'='*53:^56}')
    print (indent1*2 + 'Cardiology:')
    print (indent1*4, 'Total Beds:' + indent1*4, TOTAL_BEDS_PER_UNIT)
    print (indent1*4, 'Beds Occupied:',indent1*2, cardio_beds_occupied)
    print (indent1*4, f'Occupancy Rate:{indent1*2} {c_occupancy_rate:.0f}% {c_warning}')
    print ()
    print (indent1*2 + 'Respiratory:')
    print (indent1*4, 'Total Beds:'+ indent1*4, TOTAL_BEDS_PER_UNIT)
    print (indent1*4, 'Beds Occupied:',indent1*2, respiratory_beds_occupied)
    print (indent1*4, f'Occupancy Rate:{indent1*2} {r_occupancy_rate:.0f}% {r_warning}')
    print ()
    print (indent1*2 + 'Orthopedic:')
    print (indent1*4, 'Total Beds:'+ indent1*4, TOTAL_BEDS_PER_UNIT)
    print (indent1*4, 'Beds Occupied:',indent1*2, orthopedic_beds_occupied)
    print (indent1*4, f'Occupancy Rate:{indent1*2} {o_occupancy_rate:.0f}% {o_warning}')
    
main()
