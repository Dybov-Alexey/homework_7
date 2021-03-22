while(1):
    signal = input("Write traffic-ligts signal(Red, Yellow, Red-Yellow, Green) or write exit: ")
    if signal == 'Red':
        print('You must stand')
    elif signal == 'Yellow':
        print('Will be red soon')
    elif signal == 'Green':
        print('You can go')
    elif signal == 'Red-Yellow':
        print('Will be green soon')
    elif signal == 'exit':
        print('Be careful on roads, Bon Voyage!')
        break