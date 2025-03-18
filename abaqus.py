from abaqus import *
from abaqusConstants import *
import part, material, section, assembly, step, mesh, job

# Create a model
model = mdb.Model(name='MyModel')

# Create a part (e.g., a 2D rectangular block)
sketch = model.ConstrainedSketch(name='Sketch', sheetSize=200.0)
sketch.rectangle(point1=(0, 0), point2=(10, 5))
part = model.Part(name='Block', dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
part.BaseShell(sketch=sketch)

# Create material
material = model.Material(name='Steel')
material.Elastic(table=((210000.0, 0.3),))  # Young’s Modulus & Poisson's Ratio

# Create section and assign to the part
section = model.HomogeneousSolidSection(name='Section-1', material='Steel', thickness=1.0)
region = part.Set(faces=part.faces, name='Set-1')
part.SectionAssignment(region=region, sectionName='Section-1')

# Create assembly
assembly = model.rootAssembly
assembly.Instance(name='BlockInstance', part=part, dependent=ON)

# Create step
model.StaticStep(name='Step-1', previous='Initial')

# Create boundary condition (fix one side)
edges = part.edges.findAt(((0, 2.5, 0),))
region = assembly.instances['BlockInstance'].Set(edges=edges, name='BC-Set')
model.DisplacementBC(name='BC-1', createStepName='Initial', region=region, u1=0.0, u2=0.0)

# Create job and write input file
job = mdb.Job(name='MyJob', model='MyModel')
job.writeInput(consistencyChecking=OFF)

print("Input file 'MyJob.inp' has been generated.")
