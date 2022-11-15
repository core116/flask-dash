from fastapi import APIRouter
from zen_dash import instances as i
from zen_dash.flex_data import FlexData


router = APIRouter(
    prefix="/backend/page_one/row_nine",
    tags=["row_two"],
    responses={404: {"description": "Not found"}},
)

flex=FlexData(fxFlex="50%", fxFlex_md="50%", fxFlex_sm="110%", fxFlex_xs="110%")

@router.post("/table", response_model=i.ReturnData)
async def prf():
    return i.ReturnData(type=i.InstanceType.TABLE,
                        table_data=i.TableData(name="table_1",
                                         columns=[i.TableColumn(columnDef="name", header="Name"),
                                                  i.TableColumn(
                                             columnDef="date", header="Date"),
                                             i.TableColumn(
                                             columnDef="company", header="company"),
                                             i.TableColumn(
                                             columnDef="country", header="Country"),
                                             i.TableColumn(
                                             columnDef="city", header="City"),
                                             i.TableColumn(columnDef="phone", header="Phone")],
                                         data=[{"name": "Molly Pope",
                                                "date": "Jul 27, 2021",
                                                "company": "Faucibus Orci Institute",
                                                "country": "New Zealand",
                                                "city": "Campinas",
                                                "phone": "1-403-634-0276"},
                                               {"name": "Alfonso Vinson",
                                                "date": "May 11, 2021",
                                                "company": "Non Ante Corp.",
                                                "country": "United Kingdom",
                                                "city": "Redlands",
                                                "phone": "1-405-411-6336"},
                                               {"name": "Camden David",
                                                "date": "Aug 6, 2022",
                                                "company": "Cursus Et LLP",
                                                "country": "Nigeria",
                                                "city": "Iguala",
                                                "phone": "(415) 628-6853"},
                                               {"name": "Levi Goff",
                                                "date": "Nov 3, 2021",
                                                "company": "Vitae Incorporated",
                                                "country": "Sweden",
                                                "city": "Manavgat",
                                                "phone": "1-545-823-7985"},
                                               {"name": "Madaline Leach",
                                                "date": "Jun 13, 2022",
                                                "company": "Erat Volutpat Corp.",
                                                "country": "Chile",
                                                "city": "Niterói",
                                                "phone": "1-678-156-9674"},
                                               {"name": "Camden David",
                                                "date": "Aug 6, 2022",
                                                "company": "Cursus Et LLP",
                                                "country": "Nigeria",
                                                "city": "Iguala",
                                                "phone": "(415) 628-6853"},
                                               {"name": "Levi Goff",
                                                "date": "Nov 3, 2021",
                                                "company": "Vitae Incorporated",
                                                "country": "Sweden",
                                                "city": "Manavgat",
                                                "phone": "1-545-823-7985"},
                                               {"name": "Madaline Leach",
                                                "date": "Jun 13, 2022",
                                                "company": "Erat Volutpat Corp.",
                                                "country": "Chile",
                                                "city": "Niterói",
                                                "phone": "1-678-156-9674"},
                                               {"name": "Molly Pope",
                                                "date": "Jul 27, 2021",
                                                "company": "Faucibus Orci Institute",
                                                "country": "New Zealand",
                                                "city": "Campinas",
                                                "phone": "1-403-634-0276"},
                                               {"name": "Alfonso Vinson",
                                                "date": "May 11, 2021",
                                                "company": "Non Ante Corp.",
                                                "country": "United Kingdom",
                                                "city": "Redlands",
                                                "phone": "1-405-411-6336"},
                                               {"name": "Camden David",
                                                "date": "Aug 6, 2022",
                                                "company": "Cursus Et LLP",
                                                "country": "Nigeria",
                                                "city": "Iguala",
                                                "phone": "(415) 628-6853"},
                                               {"name": "Levi Goff",
                                                "date": "Nov 3, 2021",
                                                "company": "Vitae Incorporated",
                                                "country": "Sweden",
                                                "city": "Manavgat",
                                                "phone": "1-545-823-7985"},
                                               {"name": "Madaline Leach",
                                                "date": "Jun 13, 2022",
                                                "company": "Erat Volutpat Corp.",
                                                "country": "Chile",
                                                "city": "Niterói",
                                                "phone": "1-678-156-9674"},
                                               {"name": "Camden David",
                                                "date": "Aug 6, 2022",
                                                "company": "Cursus Et LLP",
                                                "country": "Nigeria",
                                                "city": "Iguala",
                                                "phone": "(415) 628-6853"},
                                               {"name": "Levi Goff",
                                                "date": "Nov 3, 2021",
                                                "company": "Vitae Incorporated",
                                                "country": "Sweden",
                                                "city": "Manavgat",
                                                "phone": "1-545-823-7985"},
                                               {"name": "Madaline Leach",
                                                "date": "Jun 13, 2022",
                                                "company": "Erat Volutpat Corp.",
                                                "country": "Chile",
                                                "city": "Niterói",
                                                "phone": "1-678-156-9674"}]), flex=flex)


@router.post("/iframe", response_model=i.ReturnData, response_model_exclude_none=True)
async def prf():
    return i.ReturnData(type=i.InstanceType.IFRAME, iframe_data=i.IframeData(url="https://pepy.tech/project/zen_dash"), flex=i.FlexData(fxFlex='50%', fxFlex_md='100%', fxFlex_sm='100%'))