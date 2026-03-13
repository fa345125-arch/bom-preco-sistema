@router.post("/")
def criar_funcionario(funcionario: FuncionarioCreate, db: Session = Depends(get_db)):
    novo = Funcionario(**funcionario.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@router.get("/")
def listar_funcionarios(db: Session = Depends(get_db)):
    return db.query(Funcionario).all()


# NOVA ROTA — ATUALIZAR FUNCIONÁRIO
@router.put("/{funcionario_id}")
def atualizar_funcionario(funcionario_id: int, dados: FuncionarioCreate, db: Session = Depends(get_db)):

    funcionario = db.query(Funcionario).filter(
        Funcionario.id == funcionario_id
    ).first()

    if not funcionario:
        return {"erro": "funcionário não encontrado"}

    funcionario.nome = dados.nome
    funcionario.cargo = dados.cargo
    funcionario.departamento = dados.departamento
    funcionario.salario = dados.salario
    funcionario.data_admissao = dados.data_admissao

    db.commit()

    return {"mensagem": "funcionário atualizado"}