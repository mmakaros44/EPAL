#!/usr/bin/python
# -*- coding: utf8 -*-
# Προγραμματιστής: Efstathios Iosifidis
# Παιχνίδι: Πράξεις αριθμών
# Filename: prakseis-aritmon.py
# Version: 0.1 beta

# Εισαγωγή
print 'ΠΡΑΞΕΙΣ ΑΡΙΘΜΩΝ'
print 'Στο παιχνίδι αυτό θα εισάγετε δυο αριθμούς.'
print 'Στην συνέχεια θα σας ζητηθεί ποιά μαθηματική πράξη θέλετε να κάνετε.'
print ''

# Εισαγωγή αριθμών
number1 = float(input('Δώσε ένα αριθμό: '))
number2 = float(input('Ευχαριστώ. Τώρα δώσε ακόμα ένα αριθμό: '))
print ''
print ''

# Επιλογές
print 'Τώρα που μου έδωσες δυο αριθμούς πρέπει να παίξουμε ένα παιχνίδι.'
print 'Αλλιώς δεν υπάρχει λόγος να σου ζητήσω 2 αριθμούς.'
print 'Σου βάζω στοίχημα ότι μπορώ να υπολογίσω πιο γρήγορα από εσένα όλες τις πράξεις μεταξύ των δυο αριθμών.'
print 'Μην μου δώσεις όμως 1 και 1 να σου πω ότι η πρόσθεση κάνει 2.'
print ''
print 'Το λοιπόν, τα πολλά λόγια είνει φτώχεια. Επέλεξε 1 έως 4 για να σου δώσω αποτέλεσμα για την αντίστοιχη πράξη.'
print 'Αν το έτρεξες κατά λάθος, πάτησε οποιονδήποτε άλλο αριθμό για έξοδο.'
print '1 για πρόσθεση'
print '2 για αφαίρεση'
print '3 για πολλαπλασιασμό'
print '4 για διαίρεση'
print 'Οποιονδήποτε άλλο αριθμό για έξοδο'
print''
praksi=int(input('Δώσε τον αριθμό για να σου κάνω την αντίστοιχη πράξη (1,2,3,4): '))

# Υπολογισμοί και εκτυπώσεις
if praksi == 1:
    print ''
    print 'Η πρόσθεση των αριθμών είναι:',round(number1+number2,2)
    print ''
    print 'Ευχαριστώ που χρησιμοποιήσατε το πρόγραμμα για πρόσθεση δυο αριθμών.'
    print 'Εάν θέλετε να υπολογίσετε άλλους αριθμούς, εκτελέστε ξανά το πρόγραμμα.'
elif praksi == 2:
    print ''
    print 'Η αφαίρεση του δεύτερου αριθμού από τον πρώτο είναι:',round(number1-number2,2)
    print ''
    print 'Ευχαριστώ που χρησιμοποιήσατε το πρόγραμμα για αφαίρεση δυο αριθμών.'    
    print 'Εάν θέλετε να υπολογίσετε άλλους αριθμούς, εκτελέστε ξανά το πρόγραμμα.'
elif praksi == 3:
    print ''
    print 'Ο πολλαπλασιασμός των δυο αριθμών είναι:',round(number1*number2,2)
    print ''
    print 'Ευχαριστώ που χρησιμοποιήσατε το πρόγραμμα για υπολογισμό δυο αριθμών.'
    print 'Εάν θέλετε να υπολογίσετε άλλους αριθμούς, εκτελέστε ξανά το πρόγραμμα.'
elif praksi == 4:
    print ''
    print 'Η διαίρεση των δυο αριθμών είναι:',round(number1/number2,2)
    print ''
    print 'Ευχαριστώ που χρησιμοποιήσατε το πρόγραμμα για διαίρεση δυο αριθμών.'    
    print 'Εάν θέλετε να υπολογίσετε άλλους αριθμούς, εκτελέστε ξανά το πρόγραμμα.'
else:
    print ''
    print 'Δεν παίξαμε το παιχνίδι.'
    print 'Εάν τερματίσατε κατά λάθος το πρόγραμμα, εκτελέστε ξανά το αρχείο prakseis-aritmon.py.'
print ''
print '2018 copyleft. Efstathios Iosifidis'
print 'Mail επικοινωνίας: iefstathios@gmail.com'
