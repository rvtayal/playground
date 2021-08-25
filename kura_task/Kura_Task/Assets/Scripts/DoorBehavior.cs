using UnityEngine;

public class DoorBehavior : MonoBehaviour
{
    Animator anim;
    private bool isOpen = false;

    void Start()
    {
        anim = gameObject.GetComponent<Animator>();
    }
    void Update()
    {
        
            //Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            //RaycastHit hit;
            // Casts the ray and get the first game object hit
            //Physics.Raycast(ray, out hit);
            //if (hit.distance < 5.0f)
            //{
            //    Debug.Log(hit.distance);
            //    Debug.Log("This hit at " + hit.collider);
            //}
            // anim.SetTrigger("Active");
        //}
    }

    public void Activate()
    {
        Debug.Log("In Active method");
        if (!isOpen)
        {
            anim.SetBool("isOpen", true);
        }
        else
        {
            anim.SetBool("isOpen", false);
        }
        isOpen = !isOpen;
    }
}
