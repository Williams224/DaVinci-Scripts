TrigEffCheck()
{
  TFile * Input= new TFile("Output.root");
  TTree* TheTree=(TTree*)Input->Get("DecayTreeTuple/DecayTree");
  
  Int_t B0_BKGCAT;
  TheTree->SetBranchAddress("B0_BKGCAT",&B0_BKGCAT);
  bool B0_L0HadronDecision_TOS;
  TheTree->SetBranchAddress("B0_L0HadronDecision_TOS",&B0_L0HadronDecision_TOS);
  bool B0_L0Global_TIS;
  TheTree->SetBranchAddress("B0_L0Global_TIS",&B0_L0Global_TIS);
  bool B0_Hlt1TrackAllL0Decision_TOS;
  TheTree->SetBranchAddress("B0_Hlt1TrackAllL0Decision_TOS",&B0_Hlt1TrackAllL0Decision_TOS);
  bool B0_Hlt2Topo2BodyBBDTDecision_TOS;
  TheTree->SetBranchAddress("B0_Hlt2Topo2BodyBBDTDecision_TOS",&B0_Hlt2Topo2BodyBBDTDecision_TOS);
  bool B0_Hlt2Topo3BodyBBDTDecision_TOS;
  TheTree->SetBranchAddress("B0_Hlt2Topo3BodyBBDTDecision_TOS",&B0_Hlt2Topo3BodyBBDTDecision_TOS);
  bool B0_Hlt2Topo4BodyBBDTDecision_TOS;
  TheTree->SetBranchAddress("B0_Hlt2Topo4BodyBBDTDecision_TOS",&B0_Hlt2Topo4BodyBBDTDecision_TOS);
  
  Long64_t N=TheTree->GetEntries();
  int truthn=0;
  int L0n=0;
  int L1n=0;
  int L2n=0;
  
  for(int i =0;i<N;++i){
    TheTree->GetEntry(i);
    if((B0_BKGCAT==10)){
      ++truthn;
      if( B0_L0Global_TIS==true||B0_L0HadronDecision_TOS==true){
        ++L0n;
        if(B0_Hlt1TrackAllL0Decision_TOS==true){
          ++L1n;
          if(B0_Hlt2Topo2BodyBBDTDecision_TOS==true||B0_Hlt2Topo3BodyBBDTDecision_TOS==true||B0_Hlt2Topo4BodyBBDTDecision_TOS==true){
            ++L2n;
          }
        }
      }
    }
  }
  double Dtruthn=truthn;
  std::cout<<"L0 efficiency= "<<L0n/Dtruthn<<std::endl;
  std::cout<<"L1 efficiency= "<<L1n/Dtruthn<<std::endl;
  std::cout<<"L2 efficiency= "<<L2n/Dtruthn<<std::endl;
  std::cout<<"Overall efficiency= "<<L2n/Dtruthn<<std::endl;


}

