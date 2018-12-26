from shutil import copyfile

Import("env", "projenv")

# access to global construction environment
print env

# access to project construction environment
print projenv

#copyfile(src, dst)
