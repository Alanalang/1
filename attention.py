import torch


class attention(nn.Module):

    def __init__(self,dim,n_head):

        assert dim%n_head==0

        self.dim=dim
        self.dim_head=dim/n_head
        self.n_head=n_head

        self.W_q=nn.Linear(dim,dim,bias=False)
        self.W_k=nn.Linear(dim,dim,bias=False)
        self.W_v=nn.Linear(dim,dim,bias=False)

        self.scale=1/(dim**0.5)
    
    def forward(self,x,mask):

        batch=x.size[0]

        # [batch,n,dim]
        q=self.W_q(x)
        k=self.W_k(x)
        v=self.W_v(x)

        # [batch,n,n_head,dim_head]-->[batch,n_head,n,dim_head]
        q=q.view(batch,-1,self.n_head,self.dim_head).transpose(1,2)
        k=k.view(batch,-1,self.n_head,self.dim_head).transpose(1,2)
        v=v.view(batch,-1,self.n_head,self.dim_head).transpose(1,2)

        # [batch,n_head,n,n]
        score=torch.matmul(q,k.transpose(2,3))*self.scale

        if mask:
            score=score.mask_fill(mask==0,-1e9)

        score=F.softmax(score,dim=-1)

        out=torch.matmul(score,v)

        out=out.transpose(1,2).view(batch,-1,self.dim)

        return out

