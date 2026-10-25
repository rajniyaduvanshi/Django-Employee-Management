
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from .models import Employee, Department, Company


def display(request):
    employees = Employee.objects.select_related(
        "department", "company"
    ).all().order_by("id")

    return render(request, "App2/empdata.html", {
        "employeedata": employees
    })


def addEmp(request):
    departments = Department.objects.all().order_by("name")
    companies = Company.objects.all().order_by("comp_name")

    if request.method == "POST":
        try:
            department = get_object_or_404(
                Department, id=request.POST.get("department")
            )
            company = get_object_or_404(
                Company, id=request.POST.get("company")
            )

            Employee.objects.create(
                name=request.POST.get("name", "").strip(),
                email=request.POST.get("email", "").strip(),
                age=request.POST.get("age"),
                salary=request.POST.get("salary"),
                address=request.POST.get("address", "").strip(),
                department=department,
                company=company
            )

            messages.success(request, "Employee added successfully!")
            return redirect("empdata")

        except (ValueError, TypeError, IntegrityError):
            messages.error(request, "Please enter valid employee details.")

    return render(request, "App2/form.html", {
        "department_data": departments,
        "company_data": companies
    })


def editdata(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        try:
            employee.name = request.POST.get("name", "").strip()
            employee.email = request.POST.get("email", "").strip()
            employee.age = request.POST.get("age")
            employee.salary = request.POST.get("salary")
            employee.address = request.POST.get("address", "").strip()

            employee.department = get_object_or_404(
                Department, id=request.POST.get("department")
            )
            employee.company = get_object_or_404(
                Company, id=request.POST.get("company")
            )

            employee.save()
            messages.success(request, "Employee updated successfully!")
            return redirect("empdata")

        except (ValueError, TypeError, IntegrityError):
            messages.error(request, "Please enter valid employee details.")

    return render(request, "App2/editForm.html", {
        "employee": employee,
        "department_data": Department.objects.all().order_by("name"),
        "company_data": Company.objects.all().order_by("comp_name")
    })


def deletedata(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.delete()
        messages.success(request, "Employee deleted successfully!")

    return redirect("empdata")


def department(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if name:
            try:
                Department.objects.create(name=name)
                messages.success(request, "Department added successfully!")
            except IntegrityError:
                messages.error(request, "This department already exists.")
        else:
            messages.error(request, "Enter a department name.")

        return redirect("department")

    return render(request, "App2/department.html", {
        "departments": Department.objects.all().order_by("name")
    })


def delete_department(request, id):
    item = get_object_or_404(Department, id=id)

    if request.method == "POST":
        try:
            item.delete()
            messages.success(request, "Department deleted.")
        except Exception:
            messages.error(
                request,
                "This department is assigned to employees and cannot be deleted."
            )

    return redirect("department")


def company(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if name:
            try:
                Company.objects.create(comp_name=name)
                messages.success(request, "Company added successfully!")
            except IntegrityError:
                messages.error(request, "This company already exists.")
        else:
            messages.error(request, "Enter a company name.")

        return redirect("company")

    return render(request, "App2/company.html", {
        "companies": Company.objects.all().order_by("comp_name")
    })


def edit_company(request, id):
    item = get_object_or_404(Company, id=id)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if not name:
            messages.error(request, "Enter a company name.")
        elif Company.objects.filter(comp_name=name).exclude(id=id).exists():
            messages.error(request, "This company name already exists.")
        else:
            item.comp_name = name
            item.save()
            messages.success(request, "Company name updated successfully!")
            return redirect("company")

    return render(request, "App2/company.html", {
        "companies": Company.objects.all().order_by("comp_name"),
        "edit_company": item
    })


def delete_company(request, id):
    item = get_object_or_404(Company, id=id)

    if request.method == "POST":
        try:
            item.delete()
            messages.success(request, "Company deleted.")
        except Exception:
            messages.error(
                request,
                "This company is assigned to employees and cannot be deleted."
            )

    return redirect("company")
