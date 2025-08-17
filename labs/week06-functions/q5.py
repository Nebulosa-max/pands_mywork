def readModules():
    modules = []  # collect {name, grade} dicts here

    moduleName = input("\tEnter the first Module name (blank to quit): ").strip()
    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\tEnter grade (0–100): "))
        modules.append(module)

        # ask for the next module name
        moduleName = input("\tEnter next Module name (blank to quit): ").strip()

    return modules


# quick test runner
if __name__ == "__main__":
    print(readModules())