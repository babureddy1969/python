def merge(final_output,l):
    print (final_output,l)
    for x in l:
        if x in final_output:
            final_output.insert(final_output.index(x),x)
        elif x< final_output[0]:
            final_output.insert(0,x)
        elif x> final_output[-1]:
            final_output+=[x]
        else:
            for f in final_output:
                if x < f:
                    final_output.insert(final_output.index(f),x)
                    break
    return final_output

print(merge([3,4,5],[4,5,7,9]))