from multiprocessing import context
from pydoc import render_doc
from django.shortcuts import render, get_object_or_404
from dangky.models import NguoiDung

# Create your views here.
def dangnhap(request):
    return render(request,'dangnhap.html')
    

def xuly_dangnhap(request):
    ten = request.GET.get('ten')
    mk = request.GET.get('matkhau')

    thongtin = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau =mk) 
    danh_sach =NguoiDung.objects.all()
    context = {
        'ds_nguoidung':danh_sach,
    }
    if thongtin.exists():
        return render(request, 'danhsach.html', context)
    else:
        return render(request, 'thatbai.html')
def chi_tiet(request, nguoidung_id):
    print(nguoidung_id)
    
    nv = get_object_or_404(NguoiDung, pk = nguoidung_id)
   
    return render(request, 'chitiet.html', {'nd': nv})


def xuly_capnhat(request):
    ten = request.GET.get('ten')
    mk = request.GET.get('matkhau')
    email = request.GET.get('mail')
    id_nguoidung = request.GET.get('id_nguoidung')

    NguoiDung.objects.filter(id = id_nguoidung).update(
        ten_dang_nhap = ten,
        mat_khau = mk,
        email = email
    )
    # thongtin = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau =mk) 
    danh_sach =NguoiDung.objects.all()
    context = {
        'ds_nguoidung':danh_sach,
    }
    # if thongtin.exists():
    return render(request, 'danhsach.html', context)
    # else:
    #     return render(request, 'thatbai.html')




def xoa_nguoidung(request, nguoidung_id):
    dulieu = get_object_or_404(NguoiDung, pk=nguoidung_id)
    try:
        dulieu.delete()
        danh_sach =NguoiDung.objects.all()
        context = {
            'ds_nguoidung':danh_sach,
        }
    # if thongtin.exists():
        return render(request, 'danhsach.html', context)
    # else:
    #     return render(request, 'thatbai.html')

    except:
        print("Xóa bị lỗi")