import rsa1 
import cv2
from PIL import Image
from numpy import asarray
import numpy
import copy


data_len = 0

def assign_pixel(num , num1):
    num = int (num)

    unit_place = num1%10
    num1 -= unit_place
    num1 += num

    if (int(num1) > 255):
        num1 -= 10 
    return num1


def enode_img (number , pixel) :
    number = str(number)
    if (len(number) == 2):
        number = '0' + number

    if (len(number) == 1):
        number = '00' + number    
    n1 , n2 , n3 = number
    l1 , l2 , l3 = pixel

    new_pixel = list()
    new_pixel.append(assign_pixel(n1 , l1))
    new_pixel.append(assign_pixel(n2 , l2))
    new_pixel.append(assign_pixel(n3 , l3))
    
    #print (new_pixel)
    return new_pixel

def encryptImage(str_ , data_len ,fileName='Pic_1.jpeg'):
    pixel_list = []

    image = Image.open('Pic_1.jpeg')
    np_img = numpy.array(image)
    
    count = 0 
    for i in np_img :
        for j in i :
            pixel_list.append(j)
            count += 1 
            if (count == data_len):
                break
        if (count == data_len ):
            break 

    numpy.array(pixel_list)
    new_pixel = list()

    for i in range(data_len) :
        new_pixel.append(enode_img(str_[i] , pixel_list[i]))

    count = 0 
    for i in range(len(np_img)):
        for j in range(len(np_img[i])):
            
            np_img[i][j] = copy.deepcopy(new_pixel[count])
            
            count += 1
            if(count == data_len):
                break 
        if (count == data_len):
            break

    data = Image.fromarray(np_img)
    data.save('encrypt.png')

def get_data(i):
    num1 = i[0]%10
    num2 = i[1]%10
    num3 = i[2]%10

    final_val = num1*100 + num2*10 + num3
    return final_val


def decryptImage( data_len , fileName='encrypt.png'):
    image_decrypt = Image.open(fileName)
    np_img = numpy.array(image_decrypt)

    count = 0
    pixel = list() 

    for i in range(len(np_img)):
            for j in range(len(np_img[i])):
                ##print (np_img[i][j])
                pixel.append(np_img[i][j])
                count += 1
                if(count == data_len):
                    break 
            if (count == data_len):
                break

    rsa = list ()

    for i in pixel :
        rsa.append(get_data(i))

    print (rsa)
    rsa = str(rsa)
    print(rsa1.getDecrypt(rsa[1:-1]))


def main():
    choice = input("Enter your action to be performed\n1.Encryption \n2.Decryption \n3. Exit\n")
    
    if (choice == '1'):
        data = input("Enter the data to be encrypted")
        str_ = rsa1.getEncrypt(data)
        print ("The encoded string using RSA is : ", str_)
        data_len = len(str_)
        print ("The key is : ",data_len)
        encryptImage(str_ , data_len)
    
    elif (choice == '2'):
        key = int(input("Enter the key\n"))
        decryptImage(key)
    
    else :
        print ("Damn It you had freaking one job !!!")

main()
